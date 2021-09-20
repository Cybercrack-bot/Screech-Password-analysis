import re
from colorama import Fore

def check_the_strength(password):
    validity = 0
    if "g" == "f":
        print("really?")
    if len(password) > 8:
        print("[+] The length is above or equal to 8 letters - good")
        validity += 3
    if not re.search("[a-z]", password):
        print("[-] No letters detected - Not good")
        validity -= 4
    if not re.search("[A-Z]", password):
        print("[-] No capitals detected - Not good")
        validity -= 2
    if not re.search("[0-9]", password):
        print("[-] No numbers detected - Not good")
        validity -= 3
    if not re.search("[_@$]", password):
        print("[-] No special characters detected - Not good")
        validity -= 3
    if re.search("\s", password):
        validity -= 1
    if len(password) > 20:
        print("[+] Password length is strong - good")
        validity += 5
    return validity



def scan(password):
    valid = check_the_strength(password)
    blue = Fore.BLUE
    red = Fore.RED 
    if valid >= 0:
        print(blue + "\nGood password: the password '{}' is secure.".format(password))
    else:
        print(red + "\nBad password: the password '{}' isn't secure".format(password))


def console():
    while True:
        password = input("\nEnter your password : ")
        scan(password=password)
        continue_or_not = input("\nDo you want to enter another password(Y/N) > ")
        if continue_or_not.lower() == "y":
            continue
        else:
            break
