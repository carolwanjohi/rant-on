from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db import transaction
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Rant
from .forms import UserForm, ProfileForm, RantForm

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







