from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="say hello", callback_data="hello")
    kb.button(text="about", callback_data="about")
    kb.adjust(1)

    return kb.as_markup()