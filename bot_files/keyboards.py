from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import files.text_for_answer as a_text
import telegram_DB.users_data as db
from main import database


def start_question_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text=a_text.start_test_question1_answer_option_1)
    builder.button(text=a_text.start_test_question1_answer_option_2)
    builder.adjust(2)
    return builder.as_markup(resize_keyoard=True, one_time_keyboard=True)


def review_start_form():
    builder = ReplyKeyboardBuilder()
    builder.button(text="все верно")
    builder.button(text="заполнить заново")
    builder.adjust(2)
    return builder.as_markup(resize_keyoard=True, one_time_keyboard=True)


def cities():
    from main import cities
    builder = ReplyKeyboardBuilder()
    for i in range(len(cities)):
        builder.button(text=f"{cities[i][0]}")
    builder.adjust(*([1]*len(cities)))
    return builder.as_markup(resize_keyoard=True, one_time_keyboard=True)


