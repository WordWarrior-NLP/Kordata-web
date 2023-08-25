from dotenv import load_dotenv
import os
from pydantic import BaseSettings

load_dotenv() # take environment variables from .env.

# database
DB_DB = os.getenv("DB_DB")
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_PORT = int(os.getenv("DB_PORT")) # 테스트용
DB_USER = os.getenv("DB_USER")


class Settings(BaseSettings):
    db_db: str = DB_DB
    db_host: str = DB_HOST
    db_password: str = DB_PASSWORD
    db_port: int = DB_PORT
    db_user: str = DB_USER

# https://medium.com/@mohit_kmr/production-ready-fastapi-application-from-0-to-1-part-3-a1ff8c700d9c
# https://www.linkedin.com/pulse/dotenv-files-app-security-fastapi-prince-odoi/