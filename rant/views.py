from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db import transaction
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Rant, Reaction
from .forms import UserForm, ProfileForm, RantForm
from emoji import Emoji

# Create your views here.
def index(request):
    '''
    View function to display the Google log in button
    '''
    title = 'RantOn'

    return render(request, 'registrations/login.html', {"title":title})

def Logout(request):
    '''
    View function to redirect user to index view function after logging out
    '''
    logout(request)
    return redirect(index)

@login_required
def profile(request):
    '''
    View function to display the current user's profile page after logging in
    '''
    try:
        current_user = request.user

        title = f'{current_user.username}\'s Profile'

        profile = Profile.get_single_profile(current_user.id)

        rants = Rant.get_user_rants(current_user.profile.id)

        return render(request, 'all-rants/profile.html', {"title":title, "current_user":current_user, "profile":profile, "rants":rants})

    except ObjectDoesNotExist:

        return redirect(index) 


@login_required
@transaction.atomic
def update_profile(request):
    '''
    View function to display a form for updating profile information
    '''
    try:

        current_user = request.user

        current_profile = current_user.profile

        title = 'Update Profile'

        if request.method == 'POST':

            user_form = UserForm(request.POST, instance=current_user)

            profile_form = ProfileForm(request.POST, instance=current_profile, files=request.FILES)

            if user_form.is_valid() and profile_form.is_valid:

                user_form.save()

                profile_form.save()

                return redirect(profile)

            else:

                messages.error(request, ('Please correct the error below.'))
   
        else:

            user_form = UserForm(instance=current_user)

            profile_form = ProfileForm(instance=current_profile)

            return render(request, 'all-rants/update-profile.html', {"title":title, "user_form": user_form, "profile_form":profile_form})

    except ObjectDoesNotExist:

        return redirect(index)

@login_required
def create_rant(request):
    '''
    View function to display a form for a user to create a rant 
    '''
    try:

        current_user = request.user

        title = 'Create Rant'

        current_profile = current_user.profile

        if request.method == 'POST':

            create_rant_form = RantForm(request.POST)

            if create_rant_form.is_valid:

                create_rant = create_rant_form.save(commit=False)

                create_rant.author = current_profile

                create_rant.save()

                return redirect(profile)

            else:

                messages.error(request, ('Please correct the error below.'))

        else:

            create_rant_form = RantForm()

            return render(request, 'all-rants/create-rant.html', {"title":title, "create_rant_form":create_rant_form})

    except ObjectDoesNotExist:

        return redirect(index)

@login_required
def my_rant(request, rant_id):
    '''
    View function to display the current user's single rant in full with the rant's reactions
    '''
    try:

        current_user = request.user

        current_rant = Rant.get_single_rant(rant_id)

        title = f'{current_rant.author.user.username}\'s Rant'

        current_rant_reactions = Reaction.get_rant_reactions(rant_id)

        rant_reaction_emojis = []

        for current_rant_reaction in current_rant_reactions:

            current_rant_reaction_icon = Emoji.replace(':'+current_rant_reaction.emoji_title+':')

            rant_reaction_emojis.append(current_rant_reaction_icon)

        return render(request, 'all-rants/my-rant.html', {"title":title, "rant":current_rant, "current_rant_reactions":rant_reaction_emojis})


    except ObjectDoesNotExist:

        return redirect(index)

@login_required
def other_rants(request):
    '''
    View function to display rants by other users other thatn the current user
    '''
    try:
        title = "Other Rants"

        current_user = request.user

        current_profile = current_user.profile

        all_rants = Rant.get_rants()

        current_user_rants = Rant.get_user_rants(current_profile.id)

        others_rants = []

        for rant in all_rants:

            if rant in current_user_rants:

                continue

            elif rant not in current_user_rants:

                others_rants.append(rant)

                continue

        return render(request, 'all-rants/other-rants.html', {"title":title, "others_rants":others_rants})

    except ObjectDoesNotExist:

        return redirect(index)

@login_required
def single_rant(request, rant_id):
    '''
    View function to display a specific rant in page of its own
    '''
    try:

        single_rant = Rant.get_single_rant(rant_id)

        title = f'{single_rant.author.user.username}\'s Rant'

        emoji_names = Emoji.keys()

        emoji_icons = []

        for emoji_name in emoji_names:

            emoji_icon = Emoji.replace(':'+emoji_name+':')
            emoji_icons.append(emoji_icon)

            continue

        # print(emoji_icons[0:4])
        rant_reaction_emojis = []

        rant_reactions = Reaction.get_rant_reactions(single_rant.id)

        for rant_reaction in rant_reactions:

            rant_reaction_icon = Emoji.replace(':'+rant_reaction.emoji_title+':')

            rant_reaction_emojis.append(rant_reaction_icon)

        # print(rant_reaction_emojis)

        return render(request, 'all-rants/single-rant.html', {"title":title, "rant":single_rant, "emoji_names":emoji_names,"emoji_icons":emoji_icons,"rant_reaction_emojis":rant_reaction_emojis})

    except ObjectDoesNotExist:

        return redirect(index)

@login_required
def reaction(request, title, rant_id):
    '''
    Function to save the rection for a rant in the database
    '''
    current_user = request.user

    found_rant = Rant.get_single_rant(rant_id)

    new_reaction = Reaction(user_reacting=current_user, rant=found_rant, emoji_title=title)

    new_reaction.save()

    data = {'success':'Your reaction has successfully been saved'}

    return JsonResponse(data) 








