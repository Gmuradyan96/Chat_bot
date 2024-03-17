
from aiogram import types, F, Router
from aiogram.filters.command import Command
from keyboards.simple_keyboards import kb1, kb2
import logging
import random
from utils.random_fox import fox



router = Router()





#Handler for command /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f" Hello angry master, {name} ", reply_markup=kb1)


#Handler for command /stop
@router.message(Command('end'))
async def cmd_end(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Good bye angry master, {name}",)

#Handler for command /info
@router.message(Command('info'))
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"what information you prepare? {name}")

@router.message(Command('about video games'))
async def cmd_about_video_game(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"what video games you like?  {name}")

#Handler for command /Fox
@router.message(Command('fox'))
@router.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f"Take the fox, {name}")
    await message.answer_photo(photo=img_fox)
    await bot.sendphoto(message.from_user.id, photo=img_fox)







#Handler for F. text
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user= message.text.lower()
    name = message.chat.first_name
    if "hello" in msg_user:
        await message.answer(f'Hi there,  {name}')
    elif "how are you" in msg_user:
        await message.answer(f'Good thanks ,you? , {name}')
    elif "who are you" in msg_user:
        await message.answer("😸")
    elif "show me the fox" in msg_user:
        await message.answer(f'Soo take it,  {name} ', reply_markup=kb2)
    elif "tell something about you" in msg_user:
        await message.answer(f'Maybe later,  {name}')







