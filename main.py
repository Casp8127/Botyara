# Здесь запускается бот

import asyncio
import logging

import text
import keyboard

from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message
import asyncio


BOT_TOKEN = ""
admin_chat = -1002182287942
logging.basicConfig(level=logging.basicConfig
                        (format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.INFO))

# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Меню", callback_data="start_menu"))

    await message.answer(text.start_phrase.format(name=message.from_user.full_name, reply_markup=builder.as_markup()))

    """
    Обработчик команды /start
    """



# Запуск процесса поллинга новых апдейтов
async def main() 
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
