import os,shutil,getpass,shlex
from colorama import Fore,Style

def cd(newdir):
    try:
        if len(newdir) == 2 and newdir[1] == ":":
            os.system(newdir)
            os.chdir(newdir + "/")
        else:
            os.chdir(newdir)
    except Exception as e:
        return e