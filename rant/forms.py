from django import forms
from .models import Profile, Rant
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ('username',)

class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = ('profile_pic',)

class RantForm(forms.ModelForm):

    class Meta:

        model = Rant
        
        fields = ('rant_title', 'rant_content')

