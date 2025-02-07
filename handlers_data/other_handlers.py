from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from lexicon_data.lexicon import LEXICON
from datetime import datetime as dt

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import Command, CommandStart, StateFilter
import logging
from database_data.Orm_logic import init, insert_data, output_data, drop_data, change_data

from services_data.root import player


router = Router()

@router.callback_query(F.data.in_([f'button{i}' for i in range(1, 5)]))
async def callback_messages(call:CallbackQuery):
    print(call.message.text)
    if call.data in [f'button{i}' for i in range(1, 3)]:
        if call.data == 'button1':
            if call.message.text != 'Ваше здоровье':
                await call.answer(text='Ваше здоровье',cache_time=3)
        else:
            if call.message.text != 'Ваша броня':
                await call.answer(text='Ваша броня',cache_time=3)
    else:
        if call.data == 'button3':
            if call.message.text != 'Здоровье врага':
                await call.answer(text='Здоровье врага',cache_time=3)
        else:
            if call.message.text != 'Броня врага':
                await call.answer(text='Броня врага',cache_time=3)
    await call.answer()

    

@router.message(F.text == '/show')
async def show_command_messages(message:Message):
    result = await output_data()
    await message.answer(str(result))
    print(result)


@router.message()
async def any_messages(message:Message):
    print(player.GAME_DATA)
    #print(player.__base_class)

    await message.answer('What do you want?')

