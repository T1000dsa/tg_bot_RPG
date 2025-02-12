from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from lexicon_data.lexicon import LEXICON
from datetime import datetime as dt

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import Command, CommandStart, StateFilter
import logging
from database_data.Orm_logic import init, insert_data, output_data, drop_data, change_data
from filters_data.filters import IsAdmin


router = Router()

    
@router.message(F.text == '/show', IsAdmin())
async def show_command_messages(message:Message):
    result = await output_data()
    await message.answer(str(result))


@router.message()
async def any_messages(message:Message):
    await message.answer('What do you want?')