from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon_data.lexicon import LEXICON
from services_data.fight_conculation import data_base


def init_keyboard(data:str, player_data_k:dict, id:str):

    data_player = [
    player_data_k['level'], player_data_k['hp'], 
    player_data_k['physical damage'], player_data_k['magical damage'], 
    player_data_k['physical defense'], player_data_k['magical defense'],
    player_data_k['speed'], player_data_k['luck'], 
    player_data_k['exp']
    ]
    data_buttons = data_base(data, id)
    button_1 = InlineKeyboardButton(text=f'ОЗ: {data_player[1]}',callback_data='button1')
    button_2 = InlineKeyboardButton(text=f'ОБ: {data_player[4]}',callback_data='button2')
    button_3 = InlineKeyboardButton(text=f'ОЗ Врага: {data_buttons['hp']}',callback_data='button3')
    button_4 = InlineKeyboardButton(text=f'ОБ Врага: {data_buttons['physical defense']}',callback_data='button4')

    act_1 = InlineKeyboardButton(text=f'Атака',callback_data='act1')
    act_2 = InlineKeyboardButton(text=f'Защита',callback_data='act2')
    act_3 = InlineKeyboardButton(text=f'Предмет',callback_data='act3')
    act_4 = InlineKeyboardButton(text=f'Побег',callback_data='act4')

    keyboard_main = InlineKeyboardBuilder()
    keyboard_main.row(*[button_1, button_2, button_3, button_4], width=2)
    keyboard_main.row(*[act_1, act_2, act_3, act_4], width=2)
    return keyboard_main.as_markup()
