from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db import transaction
from .models import Profile
from .forms import UserForm, ProfileForm


# Create your views here.
def index(request):
    '''
    View function to display the Google log
    '''
    title = 'RantOn'

    return render(request, 'registrations/login.html', {"title":title})

@login_required
def profile(request):
    '''
    View function to display the current user's profile page after logging in
    '''
    current_user = request.user

    title = f'{current_user.username}\s Profile'

    return render(request, 'all-rants/profile.html', {"title":title, "user":current_user})


def Logout(request):
    '''
    View function to redirect user to index view function after logging out
    '''
    logout(request)
    return redirect(index)



