import aiohttp
from app.utils.logger import logger

class AzureService:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://graph.microsoft.com/v1.0"

    async def fetch_users(self):
        url = f"{self.base_url}/users"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    error_message = await response.text()
                    logger.error(f"Failed to fetch users: {error_message}")
                    response.raise_for_status()
                data = await response.json()
                return data.get("value", [])
