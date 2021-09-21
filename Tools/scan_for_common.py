from colorama import Fore
import subprocess

def simple_scan(password):
    proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
    output = (proc.stdout.read()).decode()
    blue = Fore.BLUE
    red = Fore.RED
    with open(output + "/wordlists/small_scan_wordlist.txt", "r") as wordlist:
        wordlist = wordlist.readlines()
        matches = 0
        for phrase in wordlist:
            if password == phrase.strip():
                matches += 1
                print("\n{}Weak password: The password '{}' matches with a common password '{}'".format(red, password, phrase))
                break
            else:
                continue
        return matches


def medium_scan(password):
    proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
    output = (proc.stdout.read()).decode()
    blue = Fore.BLUE
    red = Fore.RED
    with open(output + "/wordlists/medium_scan_wordlist.txt", "r") as wordlist:
        wordlist = wordlist.readlines()
        matches = 0
        for phrase in wordlist:
            if password == phrase.strip():
                matches += 1
                print("\n{}Weak password: The password '{}' matches with a common password '{}'".format(red, password))
                break
            else:
                continue
        return matches


def advanced_scan(password):
    proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
    output = (proc.stdout.read()).decode()
    blue = Fore.BLUE
    red = Fore.RED
    with open(output + "/wordlists/advanced_scan_wordlist.txt", "r") as wordlist:
        wordlist = wordlist.readlines()
        matches = 0
        for phrase in wordlist:
            if password == phrase.strip():
                matches += 1
                print("\n{}Weak password: The password '{}' matches with a common password '{}'".format(red, password, phrase))
                break
            else:
                continue
        return matches
        


def console():
    blue = Fore.BLUE
    red = Fore.RED
    print("""

    SELECT A NUMBER FROM BELLOW

1. Simple scan
2. Medium scan
3. Advanced scan
    """)
    while True:
        option = input("\nSelect a number > ")
        option = option.strip()
        if option == "1":
            print(blue + "\n [+] YOU HAVE CHOSEN SMALL SCAN [+]")
            password = input("\nEnter you password > ")
            simple_scan(password.strip())
            continue_or_not = input("Do you want to check another(Y/N) > ")
            if continue_or_not.lower() == "y":
                continue
            else:
                break
        elif option == "2":
            print(blue + "\n [+] YOU HAVE CHOSEN MEDIUM SCAN [+]")
            password = input("\nEnter you password > ")
            matches = medium_scan(password.strip())
            if matches == 0:
                print(blue + "\n[+] Strong password: The password '{}' doesnt match with any password in this password".format(password))
                print("list, This is a secure password")
            continue_or_not = input("Do you want to check another(Y/N) > ")
            if continue_or_not.lower() == "y":
                continue
            else:
                break
        elif  option == "3":
            print(blue + "\n [+] YOU HAVE CHOSEN ADVANCED SCAN [+]")
            password = input("\nEnter you password > ")
            advanced_scan(password.strip())
            continue_or_not = input("Do you want to check another(Y/N) > ")
            if continue_or_not.lower() == "y":
                continue
            else:
                break
            
            

