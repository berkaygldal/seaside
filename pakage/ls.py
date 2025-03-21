import os,shutil,getpass,shlex
from colorama import Fore,Style

def ls():
    try:
        print(" "+str(os.listdir(os.getcwd())).replace("'", "").replace("[","").replace("]","").replace(",","\n"))
    except Exception as e:
        return e