import os,shutil,getpass,shlex
from colorama import Fore,Style

def cat(path, y, z=None):
    try:
        if y == 'r':
            with open(path, 'r', encoding='utf-8') as f:
                print(f.read())
        elif y == 'w':
            with open(path, 'w', encoding='utf-8') as f:
                f.write(z)
        elif y == 'a':
            with open(path, 'a', encoding='utf-8') as f:
                f.write(z)
    except Exception as e:
        return e