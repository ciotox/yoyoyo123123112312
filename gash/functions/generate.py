# -- Main Imports -- #
import aiohttp, random, asyncio
from itertools import cycle

# -- Colorma Imports -- #
from colorama import Fore

# -- Functions Imports -- #
from functions.helpers.configure import Api, Main, Timer
from functions.helpers.webhook import send

async def check(session, username, token):
    """
    Check username availability using Discord API
    """
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    json = {
        "username": username
    }
    
    async with session.post(Api.discord['attempt'], headers=headers, json=json) as r:
        if r.status == 200:
            data = await r.json()
            taken = data.get("taken", None)

            if taken:
                print(f"{Fore.LIGHTRED_EX}{username}{Fore.RESET}: Username is taken")
            else:
                print(f"{Fore.LIGHTGREEN_EX}{username}{Fore.RESET}: Username is available")
                await send(username)
        else:
            print(f"{Fore.LIGHTRED_EX}Failed to check{Fore.RESET} {username} ({r.status})")

async def test():
    """
    """

    async with aiohttp.ClientSession() as session:
        with open(Main.files['wordlist'], "r") as file:
            usernames = [line.strip() for line in file if len(line.strip())]

        if not usernames:
            print(f"No {Fore.YELLOW}usernames{Fore.RESET} found in the wordlist")
            return

        random.shuffle(usernames)
        with open(Main.files['tokens'], "r") as token_file:
            tokens = [line.strip() for line in token_file if line.strip()]

        if not tokens:
            print(f"No {Fore.YELLOW}tokens{Fore.RESET} found")
            return

        token = cycle(tokens)

        for username in usernames:
            headers = {"Authorization": next(token)}
            print(f"{Fore.YELLOW}Using token: {headers['Authorization']}")

            await check(session, username, headers)
            await asyncio.sleep(Timer.sleeper)