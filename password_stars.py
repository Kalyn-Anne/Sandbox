"""
On paper, write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.

password = input(")
while len(password) < MIN_PASSWORD_LENGTH
    print("error message")
    password = input(")
print("*" x len(password))

# self note
# don't forget : after while or for loops
# * is times not x in code
"""

MIN_PASSWORD_LENGTH = 6

password = input("Enter password: ")
while len(password) < MIN_PASSWORD_LENGTH:
    print("Password length invalid")
    password = input("Enter password: ")
print("*" * len(password))

