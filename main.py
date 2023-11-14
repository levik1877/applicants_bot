import telegram_DB.users_data as db
from files.token import TOKEN

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command, CommandStart, CommandObject


from random import randint
import keyboards

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name}', reply_markup=keyboards.main_kb)


# @dp.message(Command(commands=['rn', 'random_number']))
# async def random_number(message: Message, command: CommandObject):
#     a, b = [int(i) for i in command.args.split('-')]
#     rand = randint(a, b)
#     await message.reply(str(rand))


# @dp.message(F.text == 'play')
# async def play_game(message: Message):
#     x = await message.answer_dice(DiceEmoji.DICE)
#     print(x.dice.value)


@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == 'urls':
        await message.answer('This is your urls:', reply_markup=keyboards.links_kb)
    elif msg == 'special buttons':
        await message.answer('special buttons', reply_markup=keyboards.spec_kb)
    elif msg == 'calc':
        await message.answer('calc', reply_markup=keyboards.calc_kb())
    elif (msg == 'f') or (msg == 'b'):
        await message.answer(reply_markup=keyboards.calc_kb())
    else:
        await message.answer('Unknown command(')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print('On ready')
    asyncio.run(main())
