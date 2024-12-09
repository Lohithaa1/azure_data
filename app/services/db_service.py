import aiomysql
from app.utils.logger import logger

class MySQLService:
    def __init__(self, config):
        self.config = config

    async def connect(self):
        self.pool = await aiomysql.create_pool(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            db=self.config.MYSQL_DATABASE,
        )

    async def insert_user(self, user):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                query = '''
                INSERT INTO azure_users (id, display_name, email, job_title)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    display_name = VALUES(display_name),
                    email = VALUES(email),
                    job_title = VALUES(job_title);
                '''
                try:
                    await cursor.execute(query, (
                        user['id'], 
                        user['displayName'], 
                        user.get('mail', ''), 
                        user.get('jobTitle', '')
                    ))
                    await conn.commit()
                    logger.info(f"Inserted/Updated user: {user['id']}")
                except Exception as e:
                    logger.error(f"Failed to insert user: {str(e)}")
