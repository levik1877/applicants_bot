from files.config import TOKEN
import files.text_for_answer as a_text
import bot_files.keyboards as kb
import telegram_DB.users_data as db

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandObject


bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

database = db.open_database()
import time
s = ['Ростов-на-Дону', 'Москва', 'Краснодар', 'Сочи', 'Екатеринбург']
for i in range(len(s)):
    db.add_cities(database, s[i])
    time.sleep(1)
cities = db.get_cities(database)

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(a_text.start_text, reply_markup=kb.start_question_keyboard())

# @dp.message(Command(commands=['rn', 'random_number']))
# async def random_number(message: Message, command: CommandObject):
#     a, b = [int(i) for i in command.args.split('-')]
#     rand = randint(a, b)
#     await message.reply(str(rand))


# @dp.message(F.text == 'play')
# async def play_game(message: Message):
#     x = await message.answer_dice(DiceEmoji.DICE)
#     print(x.dice.value)

class States(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()
    snils = State()
    answer = State()
    u1 = State()
    u2 = State()
    u3 = State()
    u4 = State()
    u5 = State()
    city_u1 = State()
    city_u2 = State()
    city_u3 = State()
    city_u4 = State()
    city_u5 = State()
    aoe1 = State()
    aoe2 = State()
    aoe3 = State()
    aoe4 = State()
    aoe5 = State()
    aoe6 = State()
    aoe7 = State()
    aoe8 = State()
    aoe9 = State()
    aoe10 = State()
    aoe11 = State()
    aoe12 = State()
    aoe13 = State()
    aoe14 = State()
    aoe15 = State()
    aoe16 = State()
    aoe17 = State()
    aoe18 = State()
    aoe19 = State()
    aoe20 = State()
    aoe21 = State()
    aoe22 = State()
    aoe23 = State()
    aoe24 = State()
    aoe25 = State()


@dp.message(F.text == 'уже подал')
async def get_name(message: Message, state: FSMContext):
    await message.answer(text=a_text.start_test_question1_answer_1_message1)
    await message.answer(text=a_text.start_test_question1_answer_1_message2)
    await message.answer(text=a_text.start_test_question1_answer_1_message3)
    await message.answer(text=a_text.consent_to_the_processing_of_personal_data)
    await message.answer(text=a_text.start_registration)
    await message.answer(text=a_text.start_registration_question1)
    await state.set_state(States.name)


@dp.message(States.name)
async def get_surname(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=a_text.start_registration_question2)
    await state.set_state(States.surname)

#   data = await state.get_data()
#   await state.clear()


@dp.message(States.surname)
async def get_patronymic(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer(text=a_text.start_registration_question3)
    await state.set_state(States.patronymic)


@dp.message(States.patronymic)
async def get_patronymic(message: Message, state: FSMContext):
    await state.update_data(patronymic=message.text)
    await message.answer(text=a_text.start_registration_question4)
    await state.set_state(States.snils)


def check_snils(snils: str):
    try:
        if len(snils) == 14:
            if (snils[3] == '-') and (snils[7] == '-') and (snils[11] == ' '):
                snils = snils.replace('-', '')
                snils = snils.replace(' ', '')
                if len(snils) == 11:
                    int(snils)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        return False


@dp.message(States.snils)
async def get_snils(message: Message, state: FSMContext):
    if check_snils(message.text):
        await state.update_data(snils=message.text)
        data = await state.get_data()
        text = a_text.start_registration_final_review + f"Имя: {data['name']}\nФамилия: {data['surname']}\nОтчество: {data['patronymic']}\nСНИЛС: {data['snils']}"
        await message.answer(text=text, reply_markup=kb.review_start_form())
        await state.set_state(States.answer)
    else:
        await message.answer(text=a_text.start_registration_question4_error)
        await state.set_state(States.snils)


@dp.message(States.answer)
async def get_answer(message: Message, state: FSMContext):
    if message.text == "все верно":
        await message.answer(text=a_text.choice_universities_header)
        await message.answer(text=a_text.choice_first_university_city, reply_markup=kb.cities())
        await state.set_state(States.city_u1)
    elif message.text == "заполнить заново":
        await state.clear()
        await message.answer(text=a_text.start_registration_question1)
        await state.set_state(States.name)


@dp.message(States.city_u1)
async def get_u1(message: Message, state: FSMContext):
    await state.update_data(city_u1=message.text)
    await message.answer(text=a_text.choice_first_university)
    await state.set_state(States.u1)



@dp.message()
async def echo(message: Message):
    msg = message.text.lower()
    if msg == 'urls':
        pass
        # await message.answer('This is your urls:', reply_markup=keyboards.links_kb)
    else:
        await message.answer('Unknown command(')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('On ready')
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot has been stop')
