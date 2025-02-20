from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from lexicon_data.lexicon import LEXICON
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import StateFilter
from database_data.Orm_logic import init, insert_data, output_data
from database_data.models import TgUsersModel, ScoreModel
from keyboards_data.keyboard_choice import keyboard_race, construct_kb, keyboard_class
from services_data.root import level_func, HostileAction, DefenseAction, RPG, players
from services_data.scenario import plots
from keyboards_data.main_keyboard import init_keyboard
from services_data.chapter_viewer import chapter_view
from services_data.fight_conculation import data_attack, data_deffence
from lexicon_data.data_transfer import data_return, current_language
import logging
import random

logger = logging.getLogger(__name__)
router = Router()

class FSMFillsome(StatesGroup):
    choice = State()
    is_race = None
    is_class = None

class FSMcache(StatesGroup):
    race_cache = None
    class_cache = None
    player_data = None

@router.message(F.text == '/start')
async def start_message(message:Message):
    data_to_db_chat = message.chat.model_dump()
    data_to_db_user = message.from_user.model_dump()
    id_db = str(data_to_db_chat['id'])
    players[id_db]= RPG()
    players['enemys'].update({id_db:RPG()})

    username_db = data_to_db_chat['username']
    firstname_db = data_to_db_chat['first_name']
    lastname_db = data_to_db_chat['last_name']
    bio_db = data_to_db_chat['bio']
    isbot_db = data_to_db_user['is_bot']
    language_db = data_to_db_user['language_code']
    current_language['lang'] = language_db

    object = TgUsersModel(user_id=id_db,
                        username=username_db,
                        firstname=firstname_db,
                        lastname=lastname_db,
                        bio=bio_db,
                        is_bot=isbot_db,
                        language_code=language_db)
    obj_score = ScoreModel(
        parent_id=id_db,
        score=0
    )

    await init()
    result:TgUsersModel = await output_data()
    if all(map(lambda x:id_db != x.user_id, result)):
        await insert_data(object)
        await insert_data(obj_score)
    else:
        logger.info(msg=f'{id_db} {LEXICON['in_data']}')
    await message.answer(LEXICON['start'])
    await message.answer(LEXICON['start_processing'], reply_markup=keyboard_race)
    


@router.message(F.text == '/help')
async def help_message(message:Message):
    await message.answer(LEXICON['help'])


@router.callback_query(F.data[:-2] == 'butt')
async def race_choice_message(call:CallbackQuery, state: FSMContext):
    data_to_db_chat = call.message.chat.model_dump()
    id_db = str(data_to_db_chat['id'])
    player:RPG = players[id_db]
    race = LEXICON[call.data]
    repr_race = data_return(race)

    await state.set_state(FSMFillsome.choice)
    await state.update_data(race_cache=race)
    await state.update_data(player_data=player)

    player.race_choice(race)
    player_data = player.data[2]

    await call.message.edit_reply_markup()
    await call.message.answer(text='Вы хотите играть\n'
                              f'как {repr_race}?',
                              reply_markup=construct_kb())
    data = [
    player_data['level'], player_data['hp'], 
    player_data['physical damage'], player_data['magical damage'], 
    player_data['physical defense'], player_data['magical defense'],
    player_data['speed'], player_data['luck'], 
    player_data['exp']
    ]
    await call.message.answer(text=LEXICON['race_data'].format(
        key_1=repr_race, 
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
    data_to_db_chat = call.message.chat.model_dump()
    id_db = str(data_to_db_chat['id'])
    player:RPG = players[id_db]
    class_prof = LEXICON[call.data]
    repr_class = data_return(class_prof)

    await state.update_data(class_cache=class_prof)
    data_cache = await state.get_data()

    player.class_choice(class_prof)
    player_data = player.data[2]

    await call.message.edit_reply_markup()
    await call.message.answer(text='Вы хотите играть\n'
                              f'как {repr_class}?',
                              reply_markup=construct_kb())
    data = [
    player_data['level'], player_data['hp'], 
    player_data['physical damage'], player_data['magical damage'], 
    player_data['physical defense'], player_data['magical defense'],
    player_data['speed'], player_data['luck'], 
    player_data['exp']
    ]
    await call.message.answer(text=LEXICON['class_data'].format(
        key_0=repr_class,
        key_1=data_return(data_cache.get('race_cache')), 
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
    data_to_db_chat = message.chat.model_dump()
    id_db = str(data_to_db_chat['id'])
    player:RPG = players[id_db]

    data:dict = await state.get_data()
    player_data_ = data.get('player_data').data[2]
    data_cache:dict = await state.get_data()
    chapter_result = chapter_view()
    for key, i in data.items():
        if i == 1:
            if key == 'is_race':
                await state.update_data(is_race=0)
                await message.answer(text=f'Раса {data_return(data_cache.get('race_cache'))} была выбрана!\n'
                                     f'{LEXICON["class_processing"]}\n',
                                     reply_markup=keyboard_class)

            elif key == 'is_class':
                player.set_standart_stats
                await state.update_data(is_class=0)
                await message.answer(text=f'Класс {data_return(data_cache.get('class_cache'))} был выбран!\n')
                await message.answer(
                    text=plots[chapter_result]['plot'].format(
                        key_0=data_return(data_cache.get('class_cache')),
                        key_1=data_return(data_cache.get('race_cache'))
                    ), 
                    reply_markup=init_keyboard(
                        chapter_result, 
                        player_data_,
                        id_db
                    )
                            )
                

@router.callback_query(F.data.in_([f'button{i}' for i in range(1, 5)]))
async def callback_messages(call:CallbackQuery):
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


@router.callback_query(F.data.in_([f'act{i}' for i in range(1, 5)]))
async def callback_messages_action(call:CallbackQuery, state: FSMContext):
    data_to_db_chat = call.message.chat.model_dump()
    id_db = str(data_to_db_chat['id'])
    player:RPG = players[id_db]

    await state.set_state(FSMFillsome.choice) 
    data:dict = await state.get_data()
    player_data_ = data.get('player_data').data[2]
    chapter_result = chapter_view()
    data_answer = random.choice(LEXICON[call.data][player.data[1].lower()])
    if call.data == 'act1': # Attack
        result = data_attack(chapter_result, player,id_db)
        if result is None:
            await call.message.edit_reply_markup()
            await call.message.answer(
                text=f'{data_answer}'
                )
            await call.message.answer(text=f'Враг наносит урон по вам',
                reply_markup=init_keyboard(
                    chapter_result, 
                    player_data_,
                    id_db
                ))
        else:
            await call.message.edit_reply_markup()
            await call.message.answer(text=f'{result}')

    elif call.data == 'act2': # Defence
        result = data_deffence(chapter_result, player,id_db)
        if result is None:
            await call.message.edit_reply_markup()
            await call.message.answer(
                text=f'{data_answer}'
                )
            await call.message.answer(text=f'Враг наносит урон по вам',
                reply_markup=init_keyboard(
                    chapter_result, 
                    player_data_,
                    id_db
                ))
    elif call.data == 'act3': # Items
        pass
    elif call.data == 'act4': # Retreit
        pass
        
    
@router.message(F.text=='/stats')
async def charaters_stats(message:Message, state:FSMContext):
    await state.set_state(FSMFillsome.choice) 
    data_to_db_chat = message.chat.model_dump()
    id_db = str(data_to_db_chat['id'])

    data:dict = await state.get_data()
    player_data_ = data.get('player_data').data[2]
    print(players[id_db].GAME_DATA)

    await message.answer(text=f'{player_data_}')