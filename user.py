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
    def user_exists(cls, pass_word):
        for user in cls.user_details:
            if user.password == pass_word:
                return True
        return False

    @classmethod
    def display_credentials(cls):

        return cls.user_details

