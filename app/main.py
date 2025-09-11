import asyncio
import logging

from aiogram.types import BotCommand

from app.loader import bot, dp
from app.handlers import start, echo

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

async def setup_bot_commands():
    commands = [
        BotCommand(command="start", description="start"),
        BotCommand(command="help", description="help"),
    ]
    await bot.set_my_commands(commands)

async def main():
    await setup_bot_commands()
    dp.include_router(start.router)
    dp.include_router(echo.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())