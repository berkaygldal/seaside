import os,shutil,getpass,shlex
from colorama import Fore,Style

def fileexists(path):
    try:
        print(os.path.exists(path))
    except Exception as e:
        return e