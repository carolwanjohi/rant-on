from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db import transaction
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from .forms import UserForm, ProfileForm

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

        return render(request, 'all-rants/profile.html', {"title":title, "current_user":current_user, "profile":profile})

    except ObjectDoesNotExist:

        return redirect(index) 


@login_required
@transaction.atomic
def update_profile(request, user_id):
    '''
    View function to display a form for updating profile information
    '''
    try:

        current_user = request.user

        current_profile = current_user.profile

        title = f'Update {current_user.username}\'s Profile'

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







