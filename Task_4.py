"""Create a password validator function that takes in the password as its argument
and returns an integer value you can evaluate to determine the password strength.
 Using the following validators:
0 -> very weak e.g. a password with only strings
1 -> weak e.g. a password with only numbers
2 -> strong e.g. a password containing strings and numbers
3 -> very strong e.g. a password containing strings, numbers and special characters (!,@,#,$,%, etc)"""

# from getpass import getpass
from string import punctuation


def password_validator():
    password = input("Enter your new password : ")
    # p_word = getpass("Enter your new password : ")
    alpha = password.isalpha()
    alpha1 = any(x.isalpha() for x in password)
    num = password.isnumeric()
    num1 = any(x.isnumeric() for x in password)
    alpha_num = password.isalnum()
    # alpha_num1 = any(x.isalnum() for x in password)
    spec_char = ""
    validator = 0
    for i in password:
        if i in punctuation:
            spec_char = True
            break
    if spec_char and alpha1 and num1:
        validator = 3
    elif alpha1 and spec_char:
        validator = 2
    elif num1 and spec_char:
        validator = 2
    elif alpha_num:
        validator = 2
    elif alpha:
        validator = 0
    elif num:
        validator = 1

    print(validator)


password_validator()
