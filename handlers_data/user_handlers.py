from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from lexicon_data.lexicon import LEXICON

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import Command, CommandStart, StateFilter
from config_data.config import Config, load_config
from database_data.Orm_logic import init, insert_data, output_data, drop_data, change_data
from database_data.models import TgUsersORM

import logging

logger = logging.getLogger(__name__)
router = Router()

@router.message(F.text == '/start')
async def start_message(message:Message):
    await message.answer(LEXICON['start'])
    await message.answer(LEXICON['start_processing'])
    data_to_db_chat = message.chat.dict()
    data_to_db_user = message.from_user.dict()

    id_db = str(data_to_db_chat['id'])
    username_db = data_to_db_chat['username']
    firstname_db = data_to_db_chat['first_name']
    lastname_db = data_to_db_chat['last_name']
    bio_db = data_to_db_chat['bio']
    isbot_db = data_to_db_user['is_bot']
    language_db = data_to_db_user['language_code']

    object = TgUsersORM(user_id=id_db,
                        username=username_db,
                        firstname=firstname_db,
                        lastname=lastname_db,
                        bio=bio_db,
                        is_bot=isbot_db,
                        language_code=language_db)
    init()
    if id_db not in [i[1] for i in output_data()]:
        insert_data(object)
    else:
        logger.info(msg=f'{id_db} Already in database')

@router.message(F.text == '/help')
async def help_message(message:Message):
    await message.answer(LEXICON['help'])
