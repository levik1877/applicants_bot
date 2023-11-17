from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import files.text_for_answer as a_text


def start_question_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text=a_text.start_test_question1_answer_option_1)
    builder.button(text=a_text.start_test_question1_answer_option_2)
    builder.adjust(2)
    return builder.as_markup(resize_keyoard=True)
