import os,shutil,getpass,shlex,importlib.util,sys,requests,matplotlib,webview
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
from colorama import Fore, Style
import tkinter as tk
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE_DIR = os.path.join(BASE_DIR, "packages")
sys.path.append(PACKAGE_DIR)
os.makedirs(PACKAGE_DIR, exist_ok=True)

PAKAGE_PATH = os.path.join(PACKAGE_DIR, "pakage.py")

if not os.path.exists(PAKAGE_PATH):
    with open(PAKAGE_PATH, "w") as f:
        f.write('''import os
import requests

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

os.makedirs(PACKAGE_DIR, exist_ok=True)

def pakage(func, action, repo="https://raw.githubusercontent.com/berkaygldal/seaside/main/pakage/"):
    if func == "install":
        file = action + ".py"
        url = f"{repo}{file}"
        filepath = os.path.join(PACKAGE_DIR, file)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"pakage : successfully installed {action}.")
        except requests.exceptions.RequestException as e:
            print(f"pakage : error while installing: {e}")
''')

def load(file):
    filepath = os.path.join(PACKAGE_DIR, f"{file}.py")
    if os.path.exists(filepath):
        spec = importlib.util.spec_from_file_location(file, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None
while True:
    os.system("title seaside : " + getpass.getuser() + "@" + os.getcwd().split("\\")[-1])
    x = input(Fore.MAGENTA + getpass.getuser() + "@" + os.getcwd().split("\\")[-1] + Fore.WHITE + " :" + Fore.GREEN + " $ " + Style.RESET_ALL)
    if not x in {"exit", "powershell", "cmd"} and (parts := shlex.split(x)):
        cmd = parts[0].lower()
        if cmd in {"cat", "fileexists", "filesize", "isdir", "isfile", "cwd", "rename", "move", "mkdir", "rm", "copy", "ls", "cd", "info", "help", "clear", "exit"}:
            code = load(cmd)
            if code and hasattr(code, cmd):
                getattr(code, cmd)(*parts[1:])
        elif os.path.exists(os.path.join(PACKAGE_DIR, f"{cmd}.py")):
            code = load(cmd)
            if code and hasattr(code, cmd):
                getattr(code, cmd)(*parts[1:])
        else:
            print("seaside : Command not found, you can use 'help' to list all commands.")
    elif x in {"exit", "powershell", "cmd"}:
        break
