from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Default image for a new profile
DEFAULT = 'profile-pic/kakashi.jpg'

# Create your models here.
class Profile(models.Model):
    '''
    Class to define a user's profile
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to="profile-pic/", blank=True)

    def __str__(self):
        '''
        Display for profiles in profile table
        '''
        return self.user.username

    @classmethod
    def get_profiles(cls):
        '''
        Fucntion that gets all the profiles in the app

        Return
            profiles : list of all Profile obejcts in the database
        '''
        profiles = Profile.objects.all()

        return profiles

    @classmethod
    def get_single_profile(cls,user_id):
        '''
        Function that gets profiles of the specified user id

        Args:
            user_id : the user id

        Returns
            single_profile : Profile object with the specified user id
        '''

        single_profile = Profile.objects.get(user=user_id)

        return single_profile


# Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when saving a User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

