import os
import shutil
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

username = os.getlogin() # The system's username
minecraft_folder = f'C:/Users/{username}/AppData/Roaming/.minecraft'

def installmods():
    mods_folder = minecraft_folder + '/mods'

    # Detects if the mods folder even exists, if it doesn't, it creates it
    if not os.path.exists(mods_folder):
        print('Mods folder doesn\'t exist')
        print(f'{Fore.BLUE}Creating {Fore.YELLOW}mods folder{Fore.WHITE}...')
        os.mkdir(mods_folder)
        
        time.sleep(1)

    # Deletes the mods folder and creates a new one if there's already existing mods in it
    if os.listdir(mods_folder):
        print(f'Detected mods in mods folder')
        print(f'{Fore.RED}Deleting {Fore.YELLOW}mods folder{Fore.WHITE}...')

        shutil.rmtree(mods_folder, ignore_errors=True)
        
        time.sleep(5) # Added a sleep here, so that if the original mods file from the minecraft folder has a lot of mods, this would give it time to actually delete before executing the code below (Change the delay time if you want)

        print(f'{Fore.BLUE}Creating {Fore.YELLOW}mods folder{Fore.WHITE}...')
        os.mkdir(mods_folder)

        time.sleep(1)
    else:
        print('Detected no mods in mods folder')
    
    # Copies the mods minecraft mods folder
    for mod in os.listdir('./mods'):
        print(f'{Fore.BLUE}Copying {Fore.YELLOW}{mod}{Fore.WHITE}...')
        shutil.copy('./mods/' + mod, mods_folder)

def installfabric():
    fabric_folder = minecraft_folder + '/versions/fabric-loader-0.11.6-1.17.1'

    # Detects if the mods folder even exists, if it doesn't, it creates it
    if not os.path.exists(fabric_folder):
        print('Fabric folder doesn\'t exist')
        print(f'{Fore.BLUE}Creating {Fore.YELLOW}fabric folder{Fore.WHITE}...')
        os.mkdir(fabric_folder)
        
        time.sleep(1)

    # Deletes the fabric folder and creates a new one if there's already existing fabric is already installed
    if os.listdir(fabric_folder):
        print('Detected files in fabric folder')
        print(f'{Fore.RED}Deleting {Fore.YELLOW}fabric folder{Fore.WHITE}...')

        shutil.rmtree(fabric_folder, ignore_errors=True)
        
        time.sleep(5) # Added a sleep here, so that if the fabric folder from the minecraft folder is big, this would give it time to actually delete before executing the code below (Change the delay time if you want)

        print(f'{Fore.BLUE}Creating {Fore.YELLOW}fabric folder{Fore.WHITE}...')
        os.mkdir(fabric_folder)
    else:
        print('Detected no files in fabric folder')
    
    # Copies the mods minecraft fabric folder
    for mod in os.listdir('./fabric-loader-0.11.6-1.17.1'):
        print(f'{Fore.BLUE}Copying {Fore.YELLOW}{mod}{Fore.WHITE}...')
        shutil.copy('./fabric-loader-0.11.6-1.17.1/' + mod, fabric_folder)

if __name__ == "__main__":
    response = input('Start installation? (yes/no): ').lower()

    if response == 'yes':
        print(f'{Fore.GREEN}Installation starting!')

        print(f'{Fore.GREEN}Installing mods!')
        installmods()
        print(f'{Fore.GREEN}Mods installed!')

        print(f'{Fore.GREEN}Installing fabric!')
        installfabric()
        print(f'{Fore.GREEN}Fabric installed!')
        
        print(f'{Fore.GREEN}Installation completed!')
        print(f'{Fore.RED}Closing in {Fore.YELLOW}20 seconds{Fore.WHITE}!')
        time.sleep(20)
    else:
        print(f'{Fore.RED}Installation cancelled!')

# Remember to create requirements.txt
