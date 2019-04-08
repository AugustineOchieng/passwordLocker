import pyperclip
class User:
    user_details = []

    def __init__(self, account, first_name, last_name, phone_number, email_address, username, password):
        self.account = account
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.username = username
        self.password = password

    def save_user(self):
        User.user_details.append(self)

    def tearDown(self):
        User.user_details = []

    @classmethod
    def user_exists(cls, number):
        for user in cls.user_details:
            if user.phone_number == number:
                return True
        return False

    @classmethod
    def user_exists(cls, number):
        for user in cls.user_details:
            if user.phone_number == number:
                return True
        return False

    @classmethod
    def display_credentials(cls):

        return cls.user_details

    @classmethod
    def copy_email(cls, number):
      user_found = User.find_by_number(number)
      pyperclip.copy(user_found.email_address)
