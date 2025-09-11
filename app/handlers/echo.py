from aiogram import Router
from aiogram.types import Message

router = Router(name=__name__)

@router.message()
async def echo_all(message: Message):
    if message.text:
        await message.answer(f"You wrote {message.text}")
    else:
        await message.answer("I don't understand")
    