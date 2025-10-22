import sys
from pathlib import Path
from colorama import Fore, Style, init

#this code will not work's if meet spaces in path

#init colorama
init(autoreset=True)

def display_directory_structure(path, indent=0):
    try:
        #convert path str to true path
        directory = Path(path)

        #path validation 
        if not directory.is_dir():
            print(Fore.RED + f"Помилка: '{path}' не є директорією або не існує")
            return
        
        #genertae result
        for item in directory.iterdir():
            if item.is_dir():
                #folder green
                print(Fore.GREEN + ' ' * indent + item.name)
                #call to folder
                display_directory_structure(item, indent + 2)
            else:
                #name blue
                print(Fore.BLUE + ' ' * indent + item.name)

    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {str(e)}")

if __name__ == "__main__":

    # Got second arguments?
    if len(sys.argv) >1 and len(sys.argv) != 2:
        print(Fore.YELLOW + "Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    #Get path string from arg
    path_name = ' '.join(sys.argv[1:])

    display_directory_structure(path_name)