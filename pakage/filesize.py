import os,shutil,getpass,shlex
from colorama import Fore,Style

def filesize(path):
    try:
        print(os.path.getsize(path))
    except Exception as e:
        return e