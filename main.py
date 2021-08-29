import os, random

from colorama import Fore, Style

from gen import *
from logo import LOGO

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def color():
    return random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA])

def still():
    main()

def main():
    clear()
    print(color() + LOGO + Style.RESET_ALL)
    
    language = input(color() +"FakesUser ~  [ru/en]: " + Style.RESET_ALL)
    if language == "ru":
        col = int(input(color() + "FakesUser ~ Сколько штук ⟩⟩ " + Style.RESET_ALL))
        ru_generator(col)
    elif language == "en":
        col = int(input(color() + "FakeUser ~ Сколько штук  ⟩⟩ " + Style.RESET_ALL))
        en_generator(col)
    else:
        print(color() + "ERROR." + Style.RESET_ALL)
        exit()
    
    while True:
        t = input("")
        if t == "exit":
            exit()
        elif t == "still":
            still()
        elif t == "clear":
            clear()
        else:
            exit()

if __name__ == "__main__":
    main()
