from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon_data.lexicon import LEXICON
from services_data.root import player
from services_data.init import RPG
from services_data.scenario import plots

def init_keyboard(data:str):
    data_plot = plots.get(data)
    player_data = player.data[2]
    data = [
    player_data['level'], player_data['hp'], 
    player_data['physical damage'], player_data['magical damage'], 
    player_data['physical defense'], player_data['magical defense'],
    player_data['speed'], player_data['luck'], 
    player_data['exp']
    ]
    hp_enemy = data_plot['enemy']['parameters']['HP']
    dp_enemy = data_plot['enemy']['parameters']['DP']
    params = {'hp':hp_enemy,
              'physical defense':dp_enemy}

    enemy = RPG()
    enemy_stats = {i:sum([params[i], k]) if i in params else k for i, k in enemy.GAME_DATA.items()}
    button_1 = InlineKeyboardButton(text=f'ОЗ: {data[1]}',callback_data='button1')
    button_2 = InlineKeyboardButton(text=f'ОБ: {data[4]}',callback_data='button2')
    button_3 = InlineKeyboardButton(text=f'ОЗ Врага: {enemy_stats['hp']}',callback_data='button3')
    button_4 = InlineKeyboardButton(text=f'ОБ Врага: {enemy_stats['physical defense']}',callback_data='button4')

    act_1 = InlineKeyboardButton(text=f'Атака',callback_data='act1')
    act_2 = InlineKeyboardButton(text=f'Защита',callback_data='act2')
    act_3 = InlineKeyboardButton(text=f'Предмет',callback_data='act3')
    act_4 = InlineKeyboardButton(text=f'Побег',callback_data='act4')

    keyboard_main = InlineKeyboardBuilder()
    keyboard_main.row(*[button_1, button_2, button_3, button_4], width=2)
    keyboard_main.row(*[act_1, act_2, act_3, act_4], width=2)
    return keyboard_main.as_markup()
