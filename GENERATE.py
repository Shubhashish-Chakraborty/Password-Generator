import random
import string

LOWER_CASE = list(string.ascii_lowercase)
UPPER_CASE = list(string.ascii_uppercase)
DIGITS = list(string.digits) # 0 - 9
SYMBOLS = ['@', '$', '#' , '%', '_']

# SYMBOLS = list(string.punctuation) No need of so many characters


def MergeAll():

    Password_Chars = []

    for i in LOWER_CASE:
        Password_Chars.append(i)
    for i in UPPER_CASE:
        Password_Chars.append(i)
    for i in DIGITS:
        Password_Chars.append(i)
    for i in SYMBOLS:
        Password_Chars.append(i)

    return Password_Chars




def generatePassword(getNumChar):

    PASSWORD = ""

    passwordAssets = MergeAll() # A List

    for char in range(getNumChar):

        PASSWORD += random.choice(passwordAssets)
    
    return PASSWORD


NumChars = int(input("Enter Number of Characters for Your Password : "))

PASSWORD = generatePassword(NumChars)

print(PASSWORD)