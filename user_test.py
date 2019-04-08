import pyperclip
import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Twitter","Gus", "Will", "0712345678","gus@gmail.com", "gus", "gus00")

    def test_init(self):
        self.assertEqual(self.new_user.account, "Twitter")
        self.assertEqual(self.new_user.first_name, "Gus")
        self.assertEqual(self.new_user.last_name, "Will")
        self.assertEqual(self.new_user.phone_number, "0712345678")
        self.assertEqual(self.new_user.email_address, "gus@gmail.com")
        self.assertEqual(self.new_user.password, "gus00")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_details), 1)
    def test_save_multiple_contact(self):
        self.new_user.save_user()
        test_user = User("Twitter","Gus", "Will", "0712345678","gus@gmail.com", "gus", "gus00")
        test_user.save_user()
        self.assertEqual(len(User.user_details), 2)
    def tearDown(self):
        User.user_details = []
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Twitter","Gus", "Will", "0712345678", "gus@gmail.com", "gus", "gus00")
        test_user.save_user()
        self.assertEqual(len(User.user_details), 2)
    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Twitter", "Gus", "Will", "0712345678", "gus@gmail.com", "gus", "gus00")
        test_user.save_user()

        user_exists = User.user_exists("0712345678")
        self.assertTrue(user_exists)
        
    def test_display_all_users(self):
      self.assertEqual(User.display_user(),
                       User.users_details)
    def test_copy_email_address(self):

      self.new_user.save_credentials()
      User.copy_email_address("0712345678")

      self.assertEqual(self.new_user.email_address,pyperclip.paste())
if __name__ == '__main__':
    unittest.main()

    
