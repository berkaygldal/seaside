import os,shutil,getpass,shlex
from colorama import Fore,Style

def rm(target):
    try:
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)
    except Exception as e:
        return e