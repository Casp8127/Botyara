# Здесь запускается бот

import asyncio
import logging
import text
import keyboard

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


# ВАЖНО! Вставьте сюда ваш токен, полученный от @BotFather
BOT_TOKEN = "7426547076:AAGod5TnX59VeCZ8le1_CeVCPCH-XjGcC1U"

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start
    """
    await message.answer(
        text.start_phrase,
        reply_markup=keyboard.get_main_keyboard()
    )


# Хэндлер на остальные текстовые сообщения
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Я получил твое сообщение: {message.text}")

# Запуск процесса поллинга новых апдейтов
async def main():
    # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())