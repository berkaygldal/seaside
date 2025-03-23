import os,shutil,getpass,shlex
from colorama import Fore, Style

install = os.path.dirname(os.path.abspath(__file__))

def help():
    print(" " + str(os.listdir(os.path.join(install))).replace("'", "").replace("[", "").replace("]", "").replace(".py", "").replace(", __pycache__", ""))
