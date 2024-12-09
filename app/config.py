import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AZURE_TOKEN = os.getenv("AZURE_ACCESS_TOKEN")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")