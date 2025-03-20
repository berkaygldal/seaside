import os,shutil,getpass,shlex
from colorama import Fore,Style
commands = {"cat","fileexists","filesize","isdir","isfile","cwd","rename","move","mkdir","rm","copy","ls","cd","info","help","clear","exit"}

def info():
    print("""   :::::::::::::::::::::                project seaside            
       ::::::::::     ::::::::          ---------------------
             :::        :::             made by berkayguldal1
             :::        ::::            
             ::           :::::::::::   seaside is a shell replacement
         ::::                    :::::  for file managment purposes.
 ::::::::::     :::       ::  :::::     please read the documentation
:::::::::::::::   :::      ::::::       for more information.
             :::::::::        ::::       
                  ::::        ::::      you are currently running:
                ::::        :::::       seaside version 1.1
              ::::        ::::::        
            :::::::   ::::::::          © Berkay Güldal 2024-2025
        :::::::::::::::::::             All rights reserved.
       ::::::::::::::::""")
    
def cd(newdir):
    try:
        os.chdir(newdir)
    except Exception as e:
        return e

def ls():
    try:
        print(" "+str(os.listdir(os.getcwd())).replace("'", "").replace("[","").replace("]","").replace(",","\n"))
    except Exception as e:
        return e

def copy(src, dest):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)
    except Exception as e:
        return e

def rm(target):
    try:
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)
    except Exception as e:
        return e

def mkdir(dirname):
    try:
        os.mkdir(dirname)
    except Exception as e:
        return e

def move(src, dest):
    try:
        shutil.move(src, dest)
    except Exception as e:
        return e

def rename(src, dest):
    try:
        os.rename(src, dest)
    except Exception as e:
        return e

def cwd():
    try:
        print(os.getcwd())
    except Exception as e:
        return e

def isfile(path):
    try:
        print(os.path.isfile(path))
    except Exception as e:
        return e

def isdir(path):
    try:
        print(os.path.isdir(path))
    except Exception as e:
        return e

def filesize(path):
    try:
        print(os.path.getsize(path))
    except Exception as e:
        return e

def fileexists(path):
    try:
        print(os.path.exists(path))
    except Exception as e:
        return e

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

def help():
    print(" "+str(commands).replace("'", "").replace("{","").replace("}",""))

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while True:
    os.system("title seaside : "+getpass.getuser()+"@"+os.getcwd().split("\\""")[-1])
    x = input(Fore.MAGENTA+getpass.getuser()+"@"+os.getcwd().split("\\""")[-1]+Fore.WHITE+" :"+Fore.GREEN+" $ "+Style.RESET_ALL)
    if not x == "exit" and (parts := shlex.split(x)) and (cmd := parts[0].lower()) in commands:
        globals()[cmd](*parts[1:])
    elif x == "exit":
        break
    else:
        print("seaside : Command not found, you can use 'help' to list all commands.")
