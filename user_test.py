import unittest
from user import User


class TestUser(unittest.TestCase):
  def setUp(self):
    self.new_user = User("Gus", "Will", "0712345678","gus@gmail.com", "gus", "gus00")

  def test_init(self):
    self.assertEqual(self.new_user.first_name, "Gus")
    self.assertEqual(self.new_user.last_name, "Will")
    self.assertEqual(self.new_user.phone_number, "0712345678")
    self.assertEqual(self.new_user.email_address, "gus@gmail.com")
    self.assertEqual(self.new_user.password, "gus00")


if __name__ == '__main__':
  unittest.main()
