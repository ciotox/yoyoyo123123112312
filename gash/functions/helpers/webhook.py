# -- Main Imports -- #
import aiohttp

# -- Functions Imports -- #
from functions.helpers.configure import Main

async def send(username):
    """
    """

    async with aiohttp.ClientSession() as s:

        data = {
            "content": f"Available Username: {username}"
        }

        async with s.post(Main.webhooks['success'], json=data) as r:
            if r.status == 204:
                print(f"Sent to webhook ({username})")
            else:
                print(f"Failed to send to webhook for {username} ({r.status})")