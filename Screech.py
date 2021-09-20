import os, sys, colorama
import platform, subprocess

if platform.system().lower() == "linux":
    proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
    output = (proc.stdout.read()).decode()
    sys.path.append(output)
    if os.getuid() != 0:
        print(colorama.Fore.RED +
            "\n[-] We detected that you use a linux system and you must run it with"
              "'sudo' to give this admin privileges, BYE\n "
              + colorama.Fore.RESET)
        quit()
elif platform.system().lower() == "windows":
    proc = subprocess.Popen('cd', stdout=subprocess.PIPE)
    output = (proc.stdout.read()).decode()
    print(output)
    sys.path.append(output)
else:
    proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
    output = (proc.stdout.read()).decode()
    sys.path.append(output)
    if os.getuid() != 0:
        print(colorama.Fore.RED +
            "\n[-] We detected that you use a Mac system and you must run it with"
              "'sudo' to give this admin privileges, BYE\n "
              + colorama.Fore.RESET)
        quit()

from Core import Core
Core.banner()

