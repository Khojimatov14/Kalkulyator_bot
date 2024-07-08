from aiogram.types import CallbackQuery
from keyboards.inline.numbers_keyboards import numbers_keyboard
from aiogram.utils.exceptions import MessageNotModified
from loader import dp
import asyncio


@dp.callback_query_handler(lambda c: True,)
async def calc(call: CallbackQuery):
    if call.data.isdigit() or call.data == '.':
        newNumber = call['message']['text']
        if newNumber[0] == '0':
            if call.data == '.' or newNumber[:2] == '0.':
                newNumber = newNumber
            else:
                newNumber = newNumber[1:]
        topNum = ''
        for item in newNumber:
            if item.isdigit() or item in '/+-*=.':
                topNum += item

        if '=' in topNum:
            topNum = ''
        try:
            await call.message.edit_text(f"{topNum+call.data}\n_                                                  _",
                                         reply_markup=numbers_keyboard)
        except MessageNotModified:
            rem = await call.message.answer("Iltimos tugmalarni sekinroq bosing!")
            await asyncio.sleep(5)
            await rem.delete()
    elif call.data == "clear":
        try:
            await call.message.edit_text("0\n_                                                  _",
                                         reply_markup=numbers_keyboard)
        except MessageNotModified:
            pass
    elif call.data == "backSpace":
        newNumber = call['message']['text']
        topNum = ''
        for item in newNumber:
            if item.isdigit() or item in '/+-*=.':
                topNum += item
        if len(topNum) == 1:
            topNum = '0'
        else:
            topNum = topNum[0:-1]
        try:
            await call.message.edit_text(f"{topNum}\n_                                                  _",
                                         reply_markup=numbers_keyboard)
        except MessageNotModified:
            pass
    elif call.data in '/+-*':
        newNumber = call['message']['text']
        topNum = ''
        for item in newNumber:
            if item.isdigit() or item in '/+-*=.':
                topNum += item
        if '=' in topNum:
            topNum = topNum.split("=")[1] + call.data
        elif topNum[-1] in '/+-*':
            topNum = topNum[0:-1] + call.data
        elif '+' in newNumber or '-' in newNumber or '*' in newNumber or '/' in newNumber:
            topNum = f"{topNum}={eval(topNum)}"
        else:
            topNum += call.data
        try:
            await call.message.edit_text(f"{topNum}\n_                                                  _",
                                         reply_markup=numbers_keyboard)
        except MessageNotModified:
            pass
    elif call.data == '=':
        newNumber = call['message']['text']
        topNum = ''
        for item in newNumber:
            if item.isdigit() or item in '/+-*=.':
                topNum += item
        if '+' not in topNum and '-' not in topNum and '*' not in topNum and '/' not in topNum:
            topNum = eval(f"{topNum}+{topNum}")
        elif '=' in topNum:
            topNum = eval(f"{topNum.split('=')[1]}+{topNum.split('=')[1]}")
            print(topNum)
        else:
            topNum = f"{topNum}={eval(topNum)}"
        try:
            await call.message.edit_text(f"{topNum}\n_                                                  _",
                                         reply_markup=numbers_keyboard)
        except MessageNotModified:
            pass

