import os,shutil,getpass,shlex
from colorama import Fore,Style

def move(src, dest):
    try:
        shutil.move(src, dest)
    except Exception as e:
        return e