from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon_data.lexicon import LEXICON
from lexicon_data.data_transfer import data_return


def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=data_return(LEXICON[button]) if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=data_return(text),
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()

keyboard_race = create_inline_kb(2, *[f'butt_{i}'for i in range(1, 7)])
keyboard_class = create_inline_kb(1, *[f'class_{i}'for i in range(1, 4)])


def construct_kb():
    a = KeyboardButton(text=LEXICON['arg_0'])
    b = KeyboardButton(text=LEXICON['arg_1'])

    keyboard_perm = ReplyKeyboardMarkup(
        keyboard=[[a, b]], 
        resize_keyboard=True,
        one_time_keyboard=True)
    return keyboard_perm