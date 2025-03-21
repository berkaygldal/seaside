import os,shutil,getpass,shlex
from colorama import Fore,Style

def rename(src, dest):
    try:
        os.rename(src, dest)
    except Exception as e:
        return e