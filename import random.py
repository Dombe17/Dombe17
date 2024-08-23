import random
import string

def generate_password(min_lengh, numbers=True, special_character=False):
    letters =string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters =letters
    if numbers:
        characters+= digits
    if special_character:
        characters+= special
    pwd =""
    correct_answ=False
    has_numbers =False
    has_special =False
    while correct_answ or len(pwd)< min_lengh:
        new_ans =random.choice(characters)
        pwd+=new_ans
        if new_ans in digits:
            has_numbers=True
        elif new_ans in special:
            has_special=False
        correct_answ =True
        if numbers:
            correct_answ = has_numbers
        if special:
            correct_answ =correct_answ and has_special

    return pwd
min_lenght =int(input("enter the minimum lenght :"))
has_numbers =input("would you like a number (y/n)?").lower() =="y"
has_special=input("would you like a special character (y/n)").lower() =="y"
pwd =generate_password(min_lenght, has_numbers,has_special)
print(pwd)