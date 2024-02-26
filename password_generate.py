import random
import string

def pass_generate(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special_chars=string.punctuation
    characters=letters
    if numbers:
        characters +=digits
    if special_characters:
        characters +=special_chars

    pwd=""
    meets_criteria=False
    has_number=False
    has_specialchars=False

    while not meets_criteria or len(pwd) <min_length:
        new_char=random.choice(characters)
        pwd +=new_char

        if new_char in digits:
            has_number=True

        if new_char in special_chars:
            has_specialchars=True

        meets_criteria=True
        if numbers:
            meets_criteria=has_number

        if special_characters:
            meets_criteria=meets_criteria and has_specialchars
    return pwd


min_length=int(input("Enter the minimum Length: "))
has_number=input("Do you want to have numbers (y/n)? ").lower() == "y"
has_specialchars=input("Do you want your Password to have special characters (y/n)? ").lower() == "y"
pwd=pass_generate(min_length,has_number,has_specialchars)
print("The generated password is:", pwd)

