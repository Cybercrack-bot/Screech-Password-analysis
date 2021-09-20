import pwnedpasswords
from colorama import Fore


def check_pwned(password):
    red, blue = Fore.RED, Fore.BLUE
    pwned = int(pwnedpasswords.check(password))
    if pwned == 0:
        print(blue + "\n[+] Your password is secure! No leaks detected. If you still doubt this, go and do an advanced security check\n")
    else:
        print(red + "\n[-] OH NO! The password '{}' has been leaked {} times\n".format(password,str(pwned)))


def console():
    while True:
        password = input("\nEnter the password > ")
        check_pwned(password)
        continue_or_not = input("\nDo you want to check another(Y/N) > ")
        if continue_or_not.lower() == "y":
            continue
        else:
            break   
        