from files.config import TOKEN
import files.text_for_answer as a_text
import bot_files.keyboards as kb
import files.text_db as test_db

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandObject


bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    if test_db.check_user(message.from_user.id):
        await message.answer(text=f'🖐Привет, {test_db.get_user(message.from_user.id)[1]}!', reply_markup=kb.menu())
    else:
        await message.answer(text=a_text.start_text, reply_markup=kb.start_question_keyboard())

# @dp.message(Command(commands=['rn', 'random_number']))
# async def random_number(message: Message, command: CommandObject):
#     a, b = [int(i) for i in command.args.split('-')]
#     rand = randint(a, b)
#     await message.reply(str(rand))


# @dp.message(F.text == 'play')
# async def play_game(message: Message):
#     x = await message.answer_dice(DiceEmoji.DICE)
#     print(x.dice.value)

class StatesRegister(StatesGroup):
    """
    u - university
    aoe - areas_of_education
    """
    name = State()
    surname = State()
    patronymic = State()
    snils = State()
    final_check = State()


@dp.message(F.text == 'уже подал')
async def get_name(message: Message, state: FSMContext):
    await message.answer(text=a_text.start_test_question1_answer_1_message1)
    await message.answer(text=a_text.start_test_question1_answer_1_message2)
    await message.answer(text=a_text.start_test_question1_answer_1_message3)
    await message.answer(text=a_text.start_registration)
    await message.answer(text=a_text.start_registration_question1)
    await state.set_state(StatesRegister.name)


@dp.message(StatesRegister.name)
async def get_surname(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=a_text.start_registration_question2)
    await state.set_state(StatesRegister.surname)

#   data = await state.get_data()
#   await state.clear()


@dp.message(StatesRegister.surname)
async def get_patronymic(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer(text=a_text.start_registration_question3)
    await state.set_state(StatesRegister.patronymic)


@dp.message(StatesRegister.patronymic)
async def get_patronymic(message: Message, state: FSMContext):
    await state.update_data(patronymic=message.text)
    await message.answer(text=a_text.start_registration_question4)
    await state.set_state(StatesRegister.snils)


def check_snils(snils: str) -> bool:
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


@dp.message(StatesRegister.snils)
async def get_snils(message: Message, state: FSMContext):
    if check_snils(message.text):
        await state.update_data(snils=message.text)
        await message.answer(text=a_text.choice_universities_header)
        data = await state.get_data()
        await message.answer(text="‼ Теперь внимательно проверь правильность введённых данных (если что потом ты можешь изменить данные в разделе профиль)")
        await message.answer(text=f"Имя: {data['name']}\nФамилия: {data['surname']}\nОтчество: {data['patronymic']}\nСНИЛС: {data['snils']}", reply_markup=kb.register_final_check_answer())
        await state.set_state(StatesRegister.final_check)
    else:
        await message.answer(text=a_text.start_registration_question4_error)
        await state.set_state(StatesRegister.snils)


@dp.message(StatesRegister.final_check)
async def final_check(message: Message, state: FSMContext):
    if message.text == 'Всё верно':
        data = await state.get_data()
        test_db.add_user((message.from_user.id, data['name'], data['surname'], data['patronymic'], data['snils']))
        await message.answer(text='👍 Отлично! Регистрация завершена, теперь ты можешь выбрать дальнейшие действия в меню', reply_markup=kb.menu())
        await state.clear()
    elif message.text == 'Изменить данные':
        await message.answer(text="📝 Введи всё ИМЯ:")
        await state.set_state(StatesRegister.name)


class StateGetUniversities(StatesGroup):
    """
        u - university
        aoe - areas_of_education
        """
    count_selected_u = State()
    count_selected_aoe = State()
    fac = State()
    city1 = State()
    u1 = State()
    aoe1 = State()
    aoe2 = State()
    aoe3 = State()
    aoe4 = State()
    aoe5 = State()
    city2 = State()
    u2 = State()
    aoe6 = State()
    aoe7 = State()
    aoe8 = State()
    aoe9 = State()
    aoe10 = State()
    city3 = State()
    u3 = State()
    aoe11 = State()
    aoe12 = State()
    aoe13 = State()
    aoe14 = State()
    aoe15 = State()
    city4 = State()
    u4 = State()
    aoe16 = State()
    aoe17 = State()
    aoe18 = State()
    aoe19 = State()
    aoe20 = State()
    city5 = State()
    u5 = State()
    aoe21 = State()
    aoe22 = State()
    aoe23 = State()
    aoe24 = State()
    aoe25 = State()


@dp.message(F.text == 'Выбрать ВУЗы')
async def get_u_and_aoe(message: Message, state: FSMContext):
    await state.update_data(count_selected_u=0)
    await state.update_data(count_selected_aoe=0)
    await message.answer(text=f"🏛 Выбрано: {0}/5 университетов.\n👨‍🎓Выбрано {0}/25 направлений подготовки.")
    await message.answer(text="🌆 Выбери город, в котором находиться унимерситет:", reply_markup=kb.cities())
    await state.set_state(StateGetUniversities.city1)


@dp.message(StateGetUniversities.city1)
async def get_city1(message: Message, state: FSMContext):
    if message.text == 'Ростов-на-Дону':
        await message.answer(text='Выбери ВУЗ:', reply_markup=kb.rnd_u())
        await state.update_data(city1=message.text)
        await state.set_state(StateGetUniversities.u1)


@dp.message(StateGetUniversities.u1)
async def get_u1(message: Message, state: FSMContext):
    if message.text == 'Донской государственный технический университет':
        await message.answer(text='Выбери факультет:', reply_markup=kb.donstu_faculties())
        await state.update_data(u1=message.text)
        await state.set_state(StateGetUniversities.fac)


@dp.message(StateGetUniversities.fac)
async def get_fac(message: Message, state: FSMContext):
    if message.text == '09.00.00 Информатика и вычислительная техника':
        await message.answer(text='Выбери образовательную программу:', reply_markup=kb.iivt())
        await state.set_state(StateGetUniversities.aoe1)


@dp.message(StateGetUniversities.aoe1)
async def get_aoe1(message: Message, state: FSMContext):
    await state.update_data(aoe1=message.text)
    data = await state.get_data()
    await state.update_data(count_selected_u=data['count_selected_u'] + 1)
    await state.update_data(count_selected_aoe=data['count_selected_aoe'] + 1)
    data = await state.get_data()
    test_db.select_u_and_aoe(message.from_user.id, data['u1'], data['aoe1'])
    await message.answer(text=f"Выбрано: {data['count_selected_u']}/5 университетов.\nВыбрано {data['count_selected_aoe']}/25 направлений подготовки.")
    await message.answer(text="Выбери дальнейшее действие", reply_markup=kb.choice_u_and_aoe_menu(data['city1']))
    await state.clear()


@dp.message((F.text == 'Вернуться в меню') or (F.text == 'Меню') or (F.text == 'Назад')) # тут разобраться как делать вызов функции на разный текст
async def menu(message: Message):
    await message.answer(text="📟Меню:", reply_markup=kb.menu())


@dp.message(F.text == 'Профиль')
async def profile(message: Message):
    user_data1 = test_db.get_user(message.from_user.id)
    user_data2 = test_db.get_selected_u_and_aoe(message.from_user.id)
    text1 = f"👨‍🎓👩‍🎓Профиль:\n📑<b>Личные данные:</b>\nИмя: <i>{user_data1[1]}</i>\nФамилия: <i>{user_data1[2]}</i>\nОтчество: <i>{user_data1[3]}</i>\nСНИЛС: <i>{user_data1[4]}</i>\n\n"
    text2 = f"🏛<b>Отслеживаемые университеты:</b>\n{user_data2[0]}:\n    {user_data2[1]}"
    await message.answer(text=text1 + text2, reply_markup=kb.profile())


@dp.message(F.text == 'Аналитика')
async def analytics(message: Message):
    selected_u_and_aoe = test_db.get_selected_u_and_aoe(message.from_user.id)
    text = f"〽〽〽\n1) <b>{selected_u_and_aoe[0]}</b>\n{selected_u_and_aoe[1]}:\n🔻<i>Место:</i> 228 (-19 позиций)"
    await message.answer(text=text, reply_markup=kb.analytics())



# ______________________________________________________________________________________________________________________
@dp.message()
async def echo(message: Message):
    msg = message.text.lower()
    if msg == 'urls':
        pass
        # await message.answer('This is your urls:', reply_markup=keyboards.links_kb)
    else:
        await message.answer(text='Unknown command(')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('On ready')
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot has been stop')
