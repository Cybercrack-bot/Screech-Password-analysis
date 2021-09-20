from Core import Core
def shell():
    while True:
        option = input("Screech: > ")
        option = option.strip()
        if option == "1":
            quit()
        elif option == "2":
            Core.check_pswd_strength()
        elif option == "3":
            Core.scan_for_common_pswd()
        elif option == "4":
            Core.check_if_pwned()
        elif option == "5":
            information()
        elif option == "6":
            help_menu()
        


def menu():
    print("""
                                    SELECT NUMBER 
                                    FROM THE MENU



    1. Quit the framework
    2. Check password strength
    3. Scan your password to ensure that it is not a common one
    4. Check if your password has been leaked or pwned
    5. Information about the tool
    6. Help
    """)


def help_menu():
    print(Core.blue + """
    

So, you need help. Don't worry, it is simple. Type menu, then you will see a menu.
Select the number infront of the option and type the number. Hit enter. Then you will
be prompted to the relavent tool. 
                            Enjoy and stay {}Secure

    """.format(Core.magenta))


def information():
    print("""

Screech is a tool developed by CyberCrack and it is used to analyze and to make the passwords safe.
    """)
