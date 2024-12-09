import asyncio
from app.services.azure_service import AzureService
from app.services.db_service import MySQLService
from app.utils.logger import logger
from app.config import Config

async def main():
    logger.info("Starting Azure Entra to MySQL microservice...")
    config = Config()
    
    azure_service = AzureService(config.AZURE_TOKEN)
    db_service = MySQLService(config)

    while True:
        try:
            logger.info("Fetching users from Azure Entra...")
            users = await azure_service.fetch_users()
            logger.info(f"Fetched {len(users)} users.")

            for user in users:
                await db_service.insert_user(user)

            logger.info("Users successfully inserted into MySQL.")
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
        await asyncio.sleep(300)  # Run every 5 minutes

if __name__ == "__main__":
    asyncio.run(main())
