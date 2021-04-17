# register
# - first name, last name, password, email
# - generate user account


# login
# - account number & password


# bank operations

# Initializing the system
import random

# Account number is key value is [ first_name, last_name, email, password, savingsAmount ]
database = {}  # dictionary


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) press 3 to exit program.\n"))

    if have_account == 1:

        login()
    elif have_account == 2:

        register()
    elif have_account == 3:

        exit()
    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")
    is_valid_account_number = account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = input("What is your password \n")

        for account_number, user_details in database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password:
                    print("Welcome %s %s " % (user_details[0], user_details[1]))
                    bank_operations(user_details)

        print('Invalid account or password')
        login()
    else:
        init()


def account_number_validation(account_number):
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid account number, account number should be integer")
                return False
            except TypeError:
                print("Invalid account type ")
        else:
            print("Account number cannot be more than 10 digits")
            return False
    else:
        print("Account number is a required field.")
        return False


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")
    savings_amount = 0

    account_number = generation_account_number()

    database[account_number] = [first_name, last_name, email, password, savings_amount]
    print("Thank you now for your initial deposit.")
    deposit_operation(database[account_number])

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()


def bank_operations(user_savings):
    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation(user_savings)
    elif selected_option == 2:

        withdrawal_operation(user_savings)
    elif selected_option == 3:

        init()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")

    bank_operations(user_savings)


def withdrawal_operation(user_savings):
    print("withdrawal")
    amount = int(input("How much would you like to withdraw?\n"))

    if user_savings[4] - amount < 0:
        print('Not enough funds.')
        return

    user_savings[4] -= amount
    print('Current saving balance: %d' % (user_savings[4]))


def deposit_operation(user_savings):
    print("Deposit Operations")
    amount = int(input("How much would you like to deposit?\n"))

    if amount <= 0:
        print('Please enter an amount greater than zero')
        return

    user_savings[4] += amount
    print('Current saving balance: %d' % (user_savings[4]))


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


#### ACTUAL BANKING SYSTEM #####

init()