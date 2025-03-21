import os,shutil,getpass,shlex
from colorama import Fore,Style

install = os.getcwd()

def help():
    print(" "+str(os.listdir(os.path.join(install,"packages"))).replace("'", "").replace("[","").replace("]","").replace(".py", "").replace(", __pycache__", ""))