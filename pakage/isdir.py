import os,shutil,getpass,shlex
from colorama import Fore,Style

def isdir(path):
    try:
        print(os.path.isdir(path))
    except Exception as e:
        return e