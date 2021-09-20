import colorama
colorama.init(autoreset=True)
from Core import Console
from Tools import check_strength, scan_for_common, password_pwned
green = colorama.Fore.GREEN
red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
blue = colorama.Fore.BLUE
magenta = colorama.Fore.MAGENTA

def banner():
    green = colorama.Fore.GREEN
    red = colorama.Fore.RED
    yellow = colorama.Fore.YELLOW
    blue = colorama.Fore.BLUE

    result = ("""
                                        ````                       
                                ``...----------...``               
                                `.----------------------.`            
                            `.----------------------------.`         
                        `.--------------------------------.`       
                        `------------------------------------`      
                        .----------------......----------------.     
                        .-------------.``       ``.--------------.    
                    .-------------`      `       .-------------.   
                    `-------------`   `.-----.`    .-------------`  
                    --------------    `--------````.--------------  
                    `--------------`    ``...----------------------` 
                    `---------------`          ``..----------------` 
                    `-----------------.```          .--------------` 
                    `-----------------------...`     .-------------` 
                    -------------.````.--------.    .-------------  
                    `-------------     .------.`    -------------`  
                    .------------.`      ```     `.------------.   
                        .-------------.``        ``.-------------.    
                        .----------------......----------------.     
                        `------------------------------------`      
                        `.--------------------------------.`       
                            `.----------------------------.`         
                                `.----------------------.`            
                                ``...----------...``        
                                        ````                       

    """)
    print(yellow + result)
    print(blue + """
                        [+]     Screech - Password Analysis      [+]
                        [+]     Created by - {}CyberCrack{}          [+]
                                    Version - {}0.1{}     


                                {} Watch out for hackers!
                        {} Your information must not be given to them
                        {}        That's where we come in
    """.format(red, blue, colorama.Fore.LIGHTMAGENTA_EX, blue, red, green, yellow, colorama.Fore.MAGENTA))
    print("""

                                    SELECT NUMBER 
                                    FROM THE MENU



    1. Quit
    2. Check password strength
    3. Scan your password to ensure that it is not a common one
    4. Check if your password has been leaked or pwned
    5. Information about the tool
    6. Help

                        
    """)
    Console.shell()


def scan_for_common_pswd():
    scan_for_common.console()


def check_pswd_strength():
    check_strength.console()


def check_if_pwned():
    password_pwned.console()