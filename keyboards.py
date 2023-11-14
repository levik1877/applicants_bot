from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


# клавиатура под полем ввода текста
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='emogi'),
            KeyboardButton(text='Urls')
        ],
        [
            KeyboardButton(text='calc'),
            KeyboardButton(text='special buttons'),
        ]
    ],
    resize_keyboard=True, # чтоб кнопки не были огромными
    one_time_keyboard=True, # чтоб меню закрывалось после нажатия на кнопку
    input_field_placeholder="Select action", # подпись на фоне поля ввода сообщения
    # selective=True # нужно для чатов, чтобы клавиатура работала только у автора сообщения
)

# клавиатура прикреплённая к сообщению
links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="https://youtube.com"),
            InlineKeyboardButton(text="Telegram channel", url="tg://resolv?domain=pognaliofficial")
        ]
    ]
)

spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="seng location", request_location=True),
            KeyboardButton(text="seng contact", request_contact=True),
            KeyboardButton(text="create test", request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text='back')
        ]
    ],
    resize_keyboard=True
)


from random import randint
# В кнопку влазяет не более 88 символов !!!!!!!!!!!!!!!!!!!!!
def calc_kb():
    builder = ReplyKeyboardBuilder()
    for i in range(98):
        builder.button(text=f'{randint(0, 99)}.{randint(0, 99)}.{randint(0, 99)} 1234567890123456789012345678901234567890123456789012345678901234567890123456789')
    builder.button(text='b')
    builder.button(text='f')
    a = [1]*98
    builder.adjust(*a, 2)

    return builder.as_markup(resize_keyoard=True)


