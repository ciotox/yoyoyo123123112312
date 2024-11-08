# -- Main Imports -- #
import asyncio, pyfiglet

# -- Colormaa Imports -- #
from colorama import Fore

# -- Functions Imports -- #
from functions.helpers.configure import Main
from functions.check import Manager
from functions.generate import test
from functions.create import fetch

# -- UI Imports -- #
from UI.grad import gradient

async def main():
    text = pyfiglet.figlet_format("GASH", font="slant")
    gradient(text)

    token = Manager("data/tokens.txt")
    await token.load()

    while True:
        print("<- 1. Check Tokens")
        print("<- 2. Username Gen")
        print("<- 3. Create Wordlist")
        print("<- 4. Exit program")
        print("\nSelect an option: ", end='')

        choice = input().strip()

        if choice == "1":
            print("\nChecking tokens...")
            await token.check()
            break
            
        elif choice == "2":
            await test()
            break

        elif choice == "3":
            letter = input("Enter the first letter you want to generate: ")
            amount = input("Enter your letter amount (use '?' for each letter, ect...): ")
            
            words = await fetch(letter, amount)
            
            if words:
                for word in words:
                    print(word)
                
                with open(Main.files['custom'], 'w') as f:
                    for word in words:
                        f.write(word + '\n')

                gradient(f"\nCustom worldlist has been created")
            else:
                print("No words are found")
            break

        elif choice == "4":
            gradient("Thank you for using gush's username gen (created by wish)")
            await asyncio.sleep(1)
            break
        else:
            print(f"{Fore.RED}Invalid choice")