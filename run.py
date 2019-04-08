#!/usr/bin/env python3.6
from credentials import Credentials
from user import User
import random


def create_credentials(fname, lname, phone, email, username, account, password):
    '''
    Function to create a new contact
    '''
    new_credentials = Credentials(
        fname, lname, phone, email, username, account, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save contact
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a contact
    '''
    credentials.delete_credentials()


def find_credentials(acc):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_credentials_by_acc(acc)


def check_existing_user(pass_word):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exists(pass_word)


def check_existing_credentials(acc):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.credentials_exists(acc)


def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()


def main():

 while True:

                    print(
                        "Hello Welcome to your PasswordLocker app.Explore your accounts and feel free to add another. What is your name?")
                    print("What is your name\n")
                    user_name = input()

                    print(f"Hello {user_name}. what would you like to do?")
                    print('\n')

                    print("\n Login")
                    print("="*100)

                    print("+" * 100)
                    print("\n Username......")

                    print("=" * 100)
                    u_name = input()

                    print("\n Password.....")
                    print("+" * 100)
                    pass_word = input()
                    print(
                        "Use these short codes : cc - create a new account, dc - display existing accounts, fc -find an account, ex -exit your credentials ")

                    short_code = input().lower()

                    if short_code == 'cc':

                            print("New Account")
                            print("-"*10)

                            print("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()

                            print("Username ...")
                            u_name = input()

                            print(
                                "\nFor a password use  pass : to create a password OR  word : to  use computer generated password\n")
                            print(' - ' * 100)
                            pass_word = input()

                            if pass_word == 'pass':
                             print("\nEnter Password")
                            pass_word = input()

                    elif pass_word == 'word':
                            characters = "abcde01234fghILKLM56789NopqrstuvWxyz"
                            p_word = "".join(random.choice(characters)
                                             for _ in range(8))
                            print(
                                f"The computer generated password is: {p_word}\n")

                            print("Account ...")
                            acc = input()

                            # create and save new contact.
                            save_credentials(create_credentials(
                                f_name, l_name, p_number, e_address, u_name, pass_word, acc))
                            print('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print(
                                        "Here is a list of all your credentials")
                                    print('\n')

                                    for credentials in display_credentials():
                                            print(
                                                f"{credentials.account} {credentials.first_name} .....{credentials.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print(
                                        "You dont seem to have any credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_credentials(search_number):
                                    search_credentials = find_credentials(
                                        search_number)
                                    print(
                                        f" username, account, password{search_credentials.first_name} {search_credentials.last_name}")
                                    print('-' * 20)

                                    print(
                                        f"Phone number.......{search_credentials.phone_number}")
                                    print(
                                        f"Email address.......{search_credentials.email}")
                            else:
                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print(
                                "I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
