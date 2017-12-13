from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Default image for a new profile
DEFAULT = 'profile-pic/user2.png'

# Create your models here.
class Profile(models.Model):
    '''
    Class to define a user's profile
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to="profile-pic/", blank=True, default=DEFAULT)

    def __str__(self):
        '''
        Display for Profile Object in Profile table
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
        Function that gets a profile with the specified user id

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

class Rant(models.Model):
    '''
    Class to define a rant
    '''
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    rant_title = models.CharField(max_length=255)

    rant_content = models.TextField()

    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        '''
        Display for Rant Object in Rant table
        '''
        return self.author.username + '\'s rant'

    class Meta:
        '''
        Order travel plans with most recent at the top
        '''
        ordering = ['-pub_date']

    @classmethod
    def get_rants(cls):
        '''
        Function that gets all the Rant objects in the database

        Return
            rants : list of all Rant objects in the database
        '''
        rants = Rant.objects.all()

        return rants

    @classmethod
    def get_single_rant(cls,rant_id):
        '''
        Function that gets a rant with the specified rant id

        Args:
            rant_id : the rant's id

        Returns
            single_rant : Rant object with the specified rant id
        '''
        single_rant = Rant.objects.get(id=rant_id)

        return single_rant

    @classmethod
    def get_user_rants(cls, user_id):
        '''
        Function that gets rant objects with the specified user id

        Args:
            user_id : the user id

        Returns
            user_rants : List of Rant objects with the specified user id
        '''
        user_rants = Rant.objects.filter(author=user_id)

        return user_rants



