import os,shutil,getpass,shlex
from colorama import Fore,Style

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")