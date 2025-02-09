from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from lexicon_data.lexicon import LEXICON
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import Command, CommandStart, StateFilter
from database_data.Orm_logic import init, insert_data, output_data
from database_data.models import TgUsersORM
from keyboards_data.keyboard_choice import keyboard_race, construct_kb, keyboard_class
from services_data.root import level_func, player
from services_data.scenario import plots
from keyboards_data.main_keyboard import init_keyboard
import logging




logger = logging.getLogger(__name__)
router = Router()

class FSMFillsome(StatesGroup):
    choice = State()
    is_race = None
    is_class = None

class FSMcache(StatesGroup):
    race_cache = None
    class_cache = None

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
    await init()
    result = await output_data()
    if id_db not in [i[1] for i in result]:
        await insert_data(object)
    else:
        logger.info(msg=f'{id_db} {LEXICON['in_data']}')
    await message.answer(LEXICON['start'])
    await message.answer(LEXICON['start_processing'], reply_markup=keyboard_race)


@router.message(F.text == '/help')
async def help_message(message:Message):
    await message.answer(LEXICON['help'])


@router.callback_query(F.data[:-2] == 'butt')
async def race_choice_message(call:CallbackQuery, state: FSMContext):
    race = LEXICON[call.data]
    await state.set_state(FSMFillsome.choice)
    await state.update_data(race_cache=race)

    player.race_choice(race)
    player_data = player.data[2]

    await call.message.edit_reply_markup()
    await call.message.answer(text='Вы хотите играть\n'
                              f'как {race}?',
                              reply_markup=construct_kb())
    data = [
    player_data['level'], player_data['hp'], 
    player_data['physical damage'], player_data['magical damage'], 
    player_data['physical defense'], player_data['magical defense'],
    player_data['speed'], player_data['luck'], 
    player_data['exp']
    ]
    await call.message.answer(text=LEXICON['race_data'].format(
        key_1=race, 
        key_2=data[1],
        key_3=data[2],
        key_4=data[3],
        key_5=data[4],
        key_6=data[5],
        key_7=data[6],
        key_8=data[7]))
    
    await state.update_data(is_race=1)

@router.callback_query(F.data[:-2] == 'class')
async def class_choice_func(call:CallbackQuery, state: FSMContext):
    class_prof = LEXICON[call.data]

    await state.update_data(class_cache=class_prof)
    data_cache = await state.get_data()

    print(data_cache)

    player.class_choice(class_prof)
    player_data = player.data[2]

    await call.message.edit_reply_markup()
    await call.message.answer(text='Вы хотите играть\n'
                              f'как {class_prof}?',
                              reply_markup=construct_kb())
    data = [
    player_data['level'], player_data['hp'], 
    player_data['physical damage'], player_data['magical damage'], 
    player_data['physical defense'], player_data['magical defense'],
    player_data['speed'], player_data['luck'], 
    player_data['exp']
    ]

    await call.message.answer(text=LEXICON['class_data'].format(
        key_0=class_prof,
        key_1=data_cache.get('race_cache'), 
        key_2=data[1],
        key_3=data[2],
        key_4=data[3],
        key_5=data[4],
        key_6=data[5],
        key_7=data[6],
        key_8=data[7]

    ))


    await state.update_data(is_class=1)


@router.message(F.text=='No', ~StateFilter(default_state))
async def class_choiced_no(message:Message, state: FSMContext):
    data:dict = await state.get_data()
    for key, i in data.items():
        if i == 1:
            if key == 'is_race':
                await message.answer(
                    LEXICON['start_processing'], 
                    reply_markup=keyboard_race
                    )
            if key == 'is_class':
                await message.answer(
                    LEXICON['start_processing'], 
                    reply_markup=keyboard_class
                    )

@router.message(F.text==f'Yes', ~StateFilter(default_state))
async def class_choiced_yes(message:Message, state: FSMContext):
    data:dict = await state.get_data()
    data_cache:dict = await state.get_data()

    for key, i in data.items():
        if i == 1:
            if key == 'is_race':
                await state.update_data(is_race=0)
                await message.answer(text=f'Раса {data_cache.get('race_cache')} была выбрана!\n'
                                     f'{LEXICON["class_processing"]}\n',
                                     reply_markup=keyboard_class)

            elif key == 'is_class':
                await state.update_data(is_class=0)
                await message.answer(text=f'Класс {data_cache.get('class_cache')} был выбран!\n')
                await state.clear()
                await message.answer(
                    text=plots['chapter_1']['plot'].format(
                        key_0=data_cache.get('race_cache'),
                        key_1=data_cache.get('class_cache')
                    ), 
                    reply_markup=init_keyboard('chapter_1'))
