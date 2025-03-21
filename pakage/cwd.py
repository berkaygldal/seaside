import os,shutil,getpass,shlex
from colorama import Fore,Style

def cwd():
    try:
        print(os.getcwd())
    except Exception as e:
        return e