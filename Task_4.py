"""Create a password validator function that takes in the password as its argument
and returns an integer value you can evaluate to determine the password strength.
 Using the following validators:
0 -> very weak e.g. a password with only strings
1 -> weak e.g. a password with only numbers
2 -> strong e.g. a password containing strings and numbers
3 -> very strong e.g. a password containing strings, numbers and special characters (!,@,#,$,%, etc)"""

from string import punctuation


def password_validator():
    password = input("Enter your new password : ")
    alpha = password.isalpha()  # returns true if a string only contains letters
    alpha1 = any(x.isalpha() for x in password)
    num = password.isnumeric()  # returns true if a string only contains numbers
    num1 = any(x.isnumeric() for x in password)  # returns true if any of the charcater in password is alpha
    alpha_num = password.isalnum()  # returns true if a string only contains alphbets and numbers
    spec_char = ""
    validator = 0
    # checking for characters
    for i in password:
        if i in punctuation:
            spec_char = True
            break

    # scoring the passwords using validators
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
