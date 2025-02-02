from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from lexicon_data.lexicon import LEXICON
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import Command, CommandStart, StateFilter
from config_data.config import Config, load_config
from database_data.Orm_logic import init, insert_data, output_data
from database_data.models import TgUsersORM
from keyboards_data.keyboard_choice import keyboard_race, keyboard_perm, keyboard_class
from services_data.root import level_func, race_cache, class_cache, player
import logging


logger = logging.getLogger(__name__)
router = Router()

class FSMFillsome(StatesGroup):
    choice = State()
    is_race = 0
    is_class = 0


@router.message(F.text == '/start')
async def start_message(message:Message):
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
    await message.answer(LEXICON['start'])
    await message.answer(LEXICON['start_processing'], reply_markup=keyboard_race)

@router.message(F.text == '/help')
async def help_message(message:Message):
    await message.answer(LEXICON['help'])


@router.callback_query(F.data[:-2] == 'butt')
async def race_choice_message(call:CallbackQuery, state: FSMContext):
    global race_cache

    race = LEXICON[call.data]
    race_cache = race

    player.race_choice(race)
    player_data = player.data[2]

    await call.message.edit_reply_markup()

    await call.message.answer(text='Вы хотите играть\n'
                              f'как {race}?',
                              reply_markup=keyboard_perm)
    data = [
    player_data['level'], player_data['hp'], 
    player_data['physical damage'], player_data['magical damage'], 
    player_data['physical defense'], player_data['magical defense'],
    player_data['speed'], player_data['luck'], 
    player_data['exp']
    ]

    await call.message.answer(text=f'Характеристики расы {race}:\n'
                              f'Очки Здоровья: {data[1]}\n'
                              f'Физический урон: {data[2]}\n'
                              f'Магический урон: {data[3]}\n'
                              f'Физическая защита: {data[4]}\n'
                              f'Магическая защита: {data[5]}\n'
                              f'Скорость: {data[6]}\n'
                              f'Удача: {data[7]}\n'
    )
    FSMFillsome.is_race = 1
    await state.set_state(FSMFillsome.choice)

    

@router.callback_query(F.data[:-2] == 'class')
async def class_choice_func(call:CallbackQuery, state: FSMContext):
    class_prof = LEXICON[call.data]
    global class_cache
    class_cache = class_prof

    player.class_choice(class_prof)
    player_data = player.data[2]

    await call.message.edit_reply_markup()
    await call.message.answer(text='Вы хотите играть\n'
                              f'как {class_prof}?',
                              reply_markup=keyboard_perm)
    data = [
    player_data['level'], player_data['hp'], 
    player_data['physical damage'], player_data['magical damage'], 
    player_data['physical defense'], player_data['magical defense'],
    player_data['speed'], player_data['luck'], 
    player_data['exp']
    ]

    await call.message.answer(text=f'Характеристики персонажа,\n'
                              f'учитывая класс {class_prof} и расу {race_cache}:\n'
                              f'Очки Здоровья: {data[1]}\n'
                              f'Физический урон: {data[2]}\n'
                              f'Магический урон: {data[3]}\n'
                              f'Физическая защита: {data[4]}\n'
                              f'Магическая защита: {data[5]}\n'
                              f'Скорость: {data[6]}\n'
                              f'Удача: {data[7]}\n'
    )
    print(call.message.text)
    FSMFillsome.is_class = 1
    await state.set_state(FSMFillsome.choice)


@router.message(F.text=='No', ~StateFilter(default_state))
async def class_choiced_no(message:Message):
    data = (FSMFillsome.is_class, FSMFillsome.is_race)
    for i in data:
        if i == 1:
            if i == data[1]:
                await message.answer(
                    LEXICON['start_processing'], 
                    reply_markup=keyboard_race
                    )
            if i == data[0]:
                await message.answer(
                    LEXICON['start_processing'], 
                    reply_markup=keyboard_class
                    )

@router.message(F.text=='Yes', ~StateFilter(default_state))
async def class_choiced_yes(message:Message, state: FSMContext):
    data = (FSMFillsome.is_class, FSMFillsome.is_race)
    for i in data:
        if i == 1:
            if i == data[1]:
                FSMFillsome.is_race = 0
                await message.answer(text=f'Раса {race_cache} была выбрана!\n',
                                     reply_markup=keyboard_class)
                await state.clear()


            if i == data[0]:
                FSMFillsome.is_class = 0
                await message.answer(text=f'Класс {class_cache} был выбран!\n')
                await state.clear()
                await message.answer(
                    text=f'Будучи {class_cache}\n'
                    f'из раса {race_cache}, вы решаете\n'
                    'отравиться в путешествие, наполненное различными\n'
                    'угрозами для жизни.\n\n'
                    'Вы решаете, что лучше передохнуть перед долгим\n'
                    'походом на встречу приключениям\n')
