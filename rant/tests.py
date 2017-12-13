from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Rant

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

class RantTestClass(TestCase):
    '''
    Test case for the Rant class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Rant class
        '''
        # Create instance of User class
        self.james = User(username='Kiki')
        self.james.save()

        self.new_rant = Rant(author=self.james.profile ,rant_title='Cupcake', rant_content='Cupcake jelly beans chocolate cake lollipop candy powder tootsie roll dragée croissant.')

    def test_instance(self):
        '''
        Test case to check if self.new_rant in an instance of Rant class
        '''
        self.assertTrue( isinstance(self.new_rant, Rant) )

    def test_get_rants(self):
        '''
        Test case to check if all rants are gotten from the database
        '''
        self.new_rant.save()

        gotten_rants = Rant.get_rants()

        rants = Rant.objects.all()

        self.assertTrue( len(gotten_rants) == len(rants))

    def test_get_single_rant(self):
        '''
        Test case to check if a single rant is gotten from the database
        '''
        self.new_rant.save()

        gotten_rant = Rant.get_single_rant(self.new_rant.id)

        self.assertTrue( isinstance(gotten_rant, Rant))


    def test_get_user_rants(self):
        '''
        Test case to check if rants for a specific user are gotten from the database
        '''
        self.new_rant.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_rant = Rant(author=self.jane.profile, rant_title='Muffin', rant_content='I love muffin cookie lemon drops dragée. Caramels macaroon I love. Dragée jelly beans topping.')
        self.test_rant.save()

        gotten_user_rants = Rant.get_user_rants(self.jane.id)

        rants = Rant.objects.all()

        self.assertTrue( len(gotten_user_rants) != len(rants))









