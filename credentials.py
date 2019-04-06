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
