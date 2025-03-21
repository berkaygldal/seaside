import os,shutil,getpass,shlex
from colorama import Fore,Style

def copy(src, dest):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)
    except Exception as e:
        return e
