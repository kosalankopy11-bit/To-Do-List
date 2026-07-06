import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
   DATABASE_URL: str = os.getenv("DATABASE_URL")
   APP_NAME: str = os.getenv("APP_NAME", "Todo List App")


settings = Settings()
