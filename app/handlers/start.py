from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app.keyboards.inline import main_kb

router = Router(name=__name__)

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Я пример бота на aiogram 3.\nВыбери действие на кнопках ниже или напиши текст — я повторю его.",
        reply_markup=main_kb(),
    )

@router.message(Command("help"))
async def cmd_help(msg: Message):
    await msg.answer("Доступные команды:\n/start — запуск\n/help — помощь")

@router.callback_query(F.data == "hello")
async def cb_hello(cb: CallbackQuery):
    await cb.message.answer("HI")
    await cb.answer()

@router.callback_query(F.data == "about")
async def cb_about(cb: CallbackQuery):
    await cb.message.answer("Я структурный проект: handlers, keyboards, config, loader.")
    await cb.answer()