from django.test import TestCase
from profiles_api.models import UserProfile, ProfileFeedItem, UserProfileManager

class UserProfileManagerTestCase(TestCase):
    def setUp(self):
        self.objects = UserProfileManager()
    
    def test_create_user_with_invalid_email(self):
        self.assertRaises(ValueError, self.objects.create_user, email=None, name='test1 FullName', password=None)
    

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(email='test@test.com', name='test1 FullName')

    def test_user_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'test1 FullName')
    
    def test_user_str(self):
        self.assertEqual(str(self.user), 'test@test.com')


class ProfileFeedItemTestCase(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(email='test@test.com', name='test1 FullName')
        self.feed_item = ProfileFeedItem.objects.create(user_profile=self.user, status_text='Sample Status')

    def test_profile_feed_item_str(self):
        self.assertEqual(str(self.feed_item), 'Sample Status')
