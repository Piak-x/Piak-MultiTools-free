import colorama
from colorama import Fore
import requests

choice3 = print(f'''
      {Fore.YELLOW}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀      ██ ███▄    █    █████ ▒█████  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒▓██ ██ ▀█   █  ▓██    ▒██▒  ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ░▒██▓██  ▀█ ██▒ ▒████  ▒██░  ██▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄      ░██▓██▒  ▐▌██▒ ░▓█▒   ▒██   ██░
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄     ░██▒██░   ▓██░▒░▒█░   ░ ████▓▒░
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒     ░▓ ░ ▒░   ▒ ▒ ░ ▒ ░   ░ ▒░▒░▒░ 
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ▒ ░ ░░   ░ ▒░░ ░       ░ ▒ ▒░ 
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░       ▒    ░   ░ ░   ░ ░   ░ ░ ░ ▒  
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░         ░          ░ ░           ░ ░  

            ''')

choice3 = input(f'''{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}What is your webhook link?: ''')
print(Fore.RESET)
r = requests.get(choice3)
print(f'{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}Webhook Name: {Fore.WHITE}{r.json()["name"]}')
print(f'{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}Webhook ID: {Fore.WHITE}{r.json()["id"]}')
print(f'{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}Guild ID of Webhook: {Fore.WHITE}{r.json()["guild_id"]}')
print(f'{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}Channel ID of Webhook: {Fore.WHITE}{r.json()["channel_id"]}')
if r.json()['avatar'] == 'null':
          print(f'{Fore.RESET}Avatar: {Fore.WHITE} None')
else:
          avatar = f'https://cdn.discordapp.com/avatars/{r.json()["id"]}/{r.json()["avatar"]}'
          print(f'{Fore.RESET}Avatar: {Fore.WHITE}{avatar}')
print(f'{Fore.RESET}Token of Webhook :{Fore.WHITE}{r.json()["token"]}')