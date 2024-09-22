import ctypes
import os
import subprocess
import threading
import random

try:
    import pystyle
    import colored
    import colorama
    import itertools
    import asyncio
    import requests
    import selenium
    import shutil
    import requests
    import more_itertools
except ModuleNotFoundError:
    os.system("pip install pystyle")
    os.system("pip install colored")
    os.system("pip install colorama")
    os.system("pip install discord.py==1.7.3")
    os.system("pip install requests")
    os.system("pip install selenium")
    os.system("pip install pyinstaller")
    os.system("pip install requests")
    os.system("pip install more_itertools")
    os.system("pip install pywin32")
    os.system("pip install pycryptodome")
    os.system("pip install discord.py-self")

os.system("cls")
from colorama import Fore, Back, Style, init
from pystyle import *
from colored import *
from threading import Thread

def useragent():
     file_path = 'data/useragents.txt'
     
     try:
         with open(file_path, 'r') as file:
             useragents = file.readlines() 
             if useragents:
                 useragents = [agent.strip() for agent in useragents]
                 return random.choice(useragents)
             else:
                 return ''
     except FileNotFoundError:
         print("")
         return ''
     except Exception as e:
         print(f"Une erreur s'est produite lors de la lecture du fichier de user-agents : {e}")
         return ''
 
     print(useragent())

def cls():
   os.system("cls")

def execute_script(script_name):
    script_path = os.path.join('utils', script_name)
    subprocess.run(['python', script_path], check=True)

def set_console_fullscreen():
    # Obtenir le handle de la console
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    hwnd = kernel32.GetConsoleWindow()

    # Obtenir le style actuel de la fenêtre
    style = user32.GetWindowLongW(hwnd, -16)
    # Ajouter le style de plein écran
    user32.SetWindowLongW(hwnd, -16, style | 0x00040000)

    # Redimensionner la fenêtre pour qu'elle occupe tout l'écran
    user32.ShowWindow(hwnd, 3)  # SW_MAXIMIZE

import time

image = [
    f"{Fore.YELLOW}            ::      ",      
    f"{Fore.YELLOW}          -::       ",       
    f"{Fore.YELLOW}         -::        ",        
    f"{Fore.YELLOW}       --::-        ",        
    f"{Fore.YELLOW}      -::::::::::   Free Version",   
    f"{Fore.YELLOW}    =-::::::::::   Made By _piak_ ",    
    f"{Fore.YELLOW}   ===----::::      ",      
    f"{Fore.YELLOW}         -:::       ",       
    f"{Fore.YELLOW}        -::-        ",        
    f"{Fore.YELLOW}        --          ",          
    f"{Fore.YELLOW}       --           "
]

# Délai entre l'affichage de chaque ligne (en secondes)
delay = 0.3

# Affiche chaque ligne une par une avec un délai
for line in image:
    print(line)
    time.sleep(delay)
time.sleep(3)

def print_menu():
    text = """ 
                                                ╔═════════════════════════════════════════════════════════════════════════╗
                                                ║██████╗░██╗░█████╗░██╗░░██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
                                                ║██╔══██╗██║██╔══██╗██║░██╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
                                                ║██████╔╝██║███████║█████╔╝░░Dev: _piak_░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║ × = PREMIUM OPTION
                                                ║██╔═══╝░██║██╔══██║██╔═██╗░░Discord: https://discord.gg/2ez5aZ7Dqk░░░░░░░║
                                                ║██║░░░░░██║██║░░██║██║░░██╗░PayPal: https://paypal.me/piaklovepvp░░░░░░░░║
                                                ║╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
                                                ╚═════════════════════════════════════════════════════════════════════════╝
                                                                                                                          
                 (1) TOKEN AUTO LOGIN ×      (6) TOKEN DMALL ×      (11) DELETE WEBHOOK              (16) SERVER CLONER ×       (21) DISCORD MASSREPORT ×
                 (2) TOKEN NUKER             (7) TOKEN LEAVER ×     (12) SPAM WEBHOOK                (17) SERVER NUKER ×        (22) OBFUSCATOR                 
                 (3) TOKEN INFORMATIONS      (8) TOKEN JOINER ×     (13) CREATE WEBHOOKS             (18) SERVER MASSDM ×       (23) PROXY SCRAPER ×         [0] EXIT
                 (4) TOKEN GENERATOR         (9) TOKEN GRABBER ×    (14) CREATE + SPAM WEBHOOKS ×    (19) TIKTOK VIEWS ×        (24) HYPESQUAD CHANGER
                 (5) TOKEN CHECKER           (10) WEBHOOK INFO      (15) CHECK WEBHOOK               (20) SPOTIFY PREMIUM ×     (25) DOX CREATOR
    """
    print(Colorate.Horizontal(Colors.yellow_to_red, text))

def main():
    os.system("cls")
    set_console_fullscreen()
    while True:
        print_menu()
        choice = input(Colorate.Horizontal(Colors.yellow_to_red, "Enter your choice: ")).strip()

        if choice == "1":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
            
        elif choice == "2":
            cls()
            execute_script("token_nuker.py")
        elif choice == "3":
            cls()
            execute_script("token_info.py")
        elif choice == "4":
            cls()
            execute_script("token_generator.py")
        elif choice == "5":
            cls()
            execute_script("token_checker.py")
        elif choice == "6":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "7":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "8":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "9":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "10":
            cls()
            execute_script("webhook_info.py")
        elif choice == "11":
            cls()
            execute_script("webhook_deleter.py")
        elif choice == "12":
            cls()
            execute_script("webhook_spammer.py")
        elif choice == "13":
            cls()
            execute_script("webhook_creator.py")
        elif choice == "14":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "15":
            cls()
            execute_script("webhook_checker.py")
        elif choice == "16":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "17":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "18":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "19":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "20":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "21":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "22":
            cls()
            execute_script("obfuscator.py")
        elif choice == "23":
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "You don't have the premium version."))
        elif choice == "24":
            cls()
            execute_script("hypesquad.py")
        elif choice == "25":
            cls()
            execute_script("dox_creator.py")
        elif choice == "0":
            os._exit()
        else:
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice, please try again."))

if __name__ == "__main__":
    main()
