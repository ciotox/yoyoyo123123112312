# -- Main Imports -- #
import aiofiles, aiohttp, asyncio, time

# -- Colormaa Imports -- #
from colorama import Fore

# -- Functions Imports -- #
from functions.helpers.configure import Main

class Manager:
    """
    """

    def __init__(self, file: str):
        self.file = file
        self.tokens = []
        self.green = Fore.LIGHTGREEN_EX
        self.yellow = Fore.LIGHTYELLOW_EX
        self.reset = Fore.RESET
    
    async def load(self):
        """
        """

        async with aiofiles.open(self.file, 'r') as f:
            raw = [line.strip() for line in await f.readlines() if line.strip()]
            self.tokens = list(set(line.split(':')[-1] for line in raw))

    async def single(self, session, token):
        """
        """
    
        headers = {
            "Authorization": token
        }

        async with session.get('https://discord.com/api/v10/users/@me', headers=headers) as r:
            return token, r.status == 200

    async def check(self):
        """
        """

        start = time.time()
        valid = []
        invalid = []

        async with aiohttp.ClientSession() as session:
            tasks = [self.single(session, token) for token in self.tokens]
            results = await asyncio.gather(*tasks)

            for token, v in results:
                if v:
                    valid.append(token)
                else:
                    invalid.append(token)

        async with aiofiles.open(self.file, 'w') as f:
            await f.writelines(f"{token}\n" for token in valid)

        async with aiofiles.open(Main.files['invalid'], 'w') as f:
            await f.writelines(f"{token}\n" for token in invalid)

        end = time.time()
        amount = end - start

        print(f"{self.green}{len(valid)} valid tokens{self.reset} - {self.yellow}{len(invalid)} invalid tokens{self.reset} - Time Taken: {amount:.2f} seconds")
