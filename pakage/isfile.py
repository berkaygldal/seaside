import os,shutil,getpass,shlex
from colorama import Fore,Style

def isfile(path):
    try:
        print(os.path.isfile(path))
    except Exception as e:
        return e