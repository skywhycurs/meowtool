import os 
import requests
import pystyle
from pystyle import Write, Anime
from pystyle import Center 
from pystyle import Colors, Colorate
banner = '''



 ███▄ ▄███▓▓█████  ▒█████   █     █░▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██▒▀█▀ ██▒▓█   ▀ ▒██▒  ██▒▓█░ █ ░█░▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██    ▓██░▒███   ▒██░  ██▒▒█░ █ ░█ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██    ▒██ ▒▓█  ▄ ▒██   ██░░█░ █ ░█ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒   ░██▒░▒████▒░ ████▓▒░░░██▒██▓   ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▒░   ░  ░░░ ▒░ ░░ ▒░▒░▒░ ░ ▓░▒ ▒    ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░  ░      ░ ░ ░  ░  ░ ▒ ▒░   ▒ ░ ░      ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░      ░      ░   ░ ░ ░ ▒    ░   ░    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
       ░      ░  ░    ░ ░      ░                 ░ ░      ░ ░      ░  ░


                owner: https://t.me/+UmvSgaQc4hEyYTky





'''

banner2 = '''



 █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████ 
▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ 
▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███   
░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄ 
░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░
  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░
  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░   
    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░
                        ░                                   

                      Enter function:
          
            1. Start Telegram Bot`s 
            2. Start Spam Numbers
            3. about script


                

'''

Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, interval=0.010, enter=True)
print(banner2)
vibor = input()

if vibor == "1":
  os.system("python3 telegram_bot_func.py") 

if vibor == "2":
  os.system("python3 spamer.py")
if vibor == "3":
  print("это урезанная версия скрипта. Созданная челом у которого ссылка при запуске этого скрипта")
