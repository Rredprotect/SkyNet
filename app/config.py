import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    bot_token:str

def get_settings() -> Settings:
    token = os.getenv("TOKEN", "").strip()
    if not token:
        raise RuntimeError("TOKEN не найден. Укажите его в .env")
    return Settings(bot_token=token)

settings = get_settings()