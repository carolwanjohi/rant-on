from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create instance of User class
        self.james = User(username='Kiki')
        self.james.save()

        # Create instance of Profile class
        self.new_profile = Profile(user=self.james)

    def test_instance(self):
        '''
        Test case to check if self.new_profile in an instance of Profile class
        '''
        self.assertTrue( isinstance(self.new_profile, Profile) )

    def test_get_profiles(self):
        '''
        Test case to check if all profiles are gotten from the database
        '''
        gotten_profiles = Profile.get_profiles()

        profiles = Profile.objects.all()

        self.assertTrue( len(gotten_profiles) == len(profiles))

    def test_get_single_profile(self):
        '''
        Test case to check if a single profile is gotten from the database
        '''
        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane)

        gotten_profile = Profile.get_single_profile(self.jane.id)

        self.assertTrue( isinstance(gotten_profile, Profile))

