# -- Main Imports -- #
import aiohttp

# -- Functions Imports -- #
from functions.helpers.configure import Api

async def fetch(letter, pattern):
    """
    """

    async with aiohttp.ClientSession() as s, s.get(f"{Api.discord['dictionary']}?sp={letter}{pattern}&max=1000") as r:
            if r.status == 200:
                words = await r.json()
                return [word['word'] for word in words]
