from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.numbers_keyboards import numbers_keyboard

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("0\n_                                                  _", reply_markup=numbers_keyboard)
