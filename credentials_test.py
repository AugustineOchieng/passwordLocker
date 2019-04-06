import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
  def setUp(self):
    self.new_credentials = Credentials(
        "gus00", "Twitter", "Gus", "Will", "0712345678", "gus@gmail.com", "gustin")

  def test_init(self):
    self.assertEqual(self.new_credentials.current_password, "gus00")
    self.assertEqual(self.new_credentials.account, "Twitter")
    self.assertEqual(self.new_credentials.first_name, "Gus")
    self.assertEqual(self.new_credentials.last_name, "Will")
    self.assertEqual(self.new_credentials.phone_number, "0712345678")
    self.assertEqual(self.new_credentials.email_address, "gus@gmail.com")
    self.assertEqual(self.new_credentials.username, "gustin")

  def test_save_credentials(self):
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_details), 1)

  def test_save_multiple_credentials(self):
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Twitter", "Gus", "Will", "0712345678",
                         "gus@gmail.com", "gus", "gus00")
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_details), 2)

  def tearDown(self):
     Credentials.credentials_details = []

  def test_credentials_exists(self):
      self.new_credentials.save_credentials()
      test_credentials = Credentials("Twitter", "Gus", "Will", "0712345678", "gus@gmail.com", "gus", "gus00")
      test_credentials.save_credentials()

      credentials_exists = Credentials.credentials_exists("0712345678")
      self.assertTrue(credentials_exists)

  def test_display_all_credentials(self):
      self.assertEqual(Credentials.display_credentials(),Credentials.credentials_details)

if __name__ == '__main__':
    unittest.main()
