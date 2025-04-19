from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '7881205126:AAHRTPqK9V20sj2YGIDmv7v6V4LkjhwR4MU'  # 🔁 Убедись, что тут настоящий токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def send_custom_link(message: types.Message):
    user = message.from_user
    if user.username:
        username = user.username
        link = f"https://t.me/{username}?text=Привет, нашел тебя на Знакомства Москва 🌸"
        hyperlink = f'<a href="{link}">@{username}</a>'  # HTML-ссылка
        await message.reply(
            f"Вот твоя ссылка:\n{hyperlink}",
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )
    else:
        await message.reply("У тебя не установлен username в Telegram 😕")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
