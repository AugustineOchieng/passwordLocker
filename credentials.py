import pyperclip
class Credentials:
   credentials_details = []

   def __init__(self, current_password, account, first_name, last_name, phone_number, email_address, username):
     self.current_password = current_password
     self.account = account
     self.first_name = first_name
     self.last_name = last_name
     self.phone_number = phone_number
     self.email_address = email_address
     self.username = username

   def save_credentials(self):
        Credentials.credentials_details.append(self)

   def tearDown(self):
        Credentials.credentials_details = []

   @classmethod
   def credentials_exists(cls, number):
        for credentials in cls.credentials_details:
            if credentials.phone_number == number:
                return True
        return False

   @classmethod
   def display_contacts(cls):
        
        return cls.credentials_details
   def test_copy_email(self):
      self.new_credentials.save_credentials()
      Credentials.copy_email("0712345678")

      self.assertEqual(self.new_credentials.email, pyperclip.paste())
