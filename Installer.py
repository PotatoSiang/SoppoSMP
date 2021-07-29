import os
import shutil
import time

def installmods():
    username = os.getlogin() # The system's username
    minecraft_folder = f'C:/Users/{username}/AppData/Roaming/.minecraft'
    mods_folder = minecraft_folder + '/mods'

    # Deletes the mods folder and creates a new one if there's already existing mods in it
    if os.listdir(mods_folder):
        print('Detected mods in mods folder')
        print('Deleting mods folder...')

        shutil.rmtree(mods_folder, ignore_errors=True)
        
        time.sleep(5) # Added a sleep here, so that if the original mods file from the minecraft folder has a lot of mods, this would give it time to actually delete before executing the code below (Change the delay time if you want)

        print('Creating a new mods folder...')
        os.mkdir(mods_folder)
    else:
        print('Detected no mods in mods folder')
    
    # Copies the mods minecraft mods folder
    for mod in os.listdir('./mods'):
        print('Copying {}...'.format(mod))
        shutil.copy('./mods/' + mod, mods_folder)

def installfabric():
    username = os.getlogin() # The system's username
    minecraft_folder = f'C:/Users/{username}/AppData/Roaming/.minecraft'
    fabric_folder = minecraft_folder + '/versions/fabric-loader-0.11.6-1.17.1'

    # Deletes the fabric folder and creates a new one if there's already existing fabric is already installed
    if os.listdir(fabric_folder):
        print('Detected fabric in versions folder')
        print('Deleting fabric folder...')

        shutil.rmtree(fabric_folder, ignore_errors=True)
        
        time.sleep(5) # Added a sleep here, so that if the fabric folder from the minecraft folder is big, this would give it time to actually delete before executing the code below (Change the delay time if you want)

        print('Creating a new fabric folder...')
        os.mkdir(fabric_folder)
    else:
        print('Detected no mods in mods folder')
    
    # Copies the mods minecraft fabric folder
    for mod in os.listdir('./fabric-loader-0.11.6-1.17.1'):
        print('Copying {}...'.format(mod))
        shutil.copy('.fabric-loader-0.11.6-1.17.1/' + mod, fabric_folder)

if __name__ == "__main__":
    response = input('Start installation? (yes/no): ').lower()

    if response == 'yes':
        print('Installation starting!')

        print('Installing mods!')
        installmods()
        print('Mods installed!')

        print('Installing fabric!')
        installfabric()
        print('Fabric installed!')
        
        print('Installation completed!')
        print('Closing in 20 seconds!')
        time.sleep(20)
    else:
        print('Installation cancelled!')
