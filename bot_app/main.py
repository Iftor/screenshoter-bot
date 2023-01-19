import telebot
from telebot.types import Message

from bot_app import settings
from bot_app.src.core import ScreenshotMaker


bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.send_message(message.chat.id, 'Введите адрес веб-страницы')


@bot.message_handler(regexp=r'^(https?://)?([\w-]{1,32}\.[\w-]{1,32})[^\s@]*$')
def handle_text(message: Message):
    try:
        screenshot_maker = ScreenshotMaker(message.text)
        status_code, screenshot = screenshot_maker.run()
        bot.send_photo(message.chat.id, screenshot, caption=f'Код ответа: {status_code}')
    except NameError as exc:
        bot.send_message(message.chat.id, 'Введите существующий адрес')
    except Exception as exc:
        bot.send_message(message.chat.id, 'Что-то пошло не так')


@bot.message_handler()
def not_url(message: Message):
    bot.send_message(message.chat.id, 'Введите адрес веб-страницы')


bot.polling(none_stop=True, interval=0)
