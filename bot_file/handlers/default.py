from aiogram import types
from random import randrange
from ..loader import bot, dp
from ..keyboards.default_kb import markup

HELP_TEXT = """
Привет 👋, я бот по продаже различных товаров! У нас есть такие команды как:
**********************************************
<b>/start</b> - запуск бота 🚀
<b>/help</b> - помощь по командам бота 💬
<b>/description</> - адрес, контактные данные, график работы 🕒
<b>/catalog</b> - список товаров которые можно купить 📒
**********************************************
"""


# @dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    try:
        await bot.send_message(chat_id=message.chat.id,
                               text="Привет ✋, я бот по продаже различных товаров! "
                                    "У меня вы можете купить все что захотите, чтобы увидеть список "
                                    "товаров которые у меня есть нажмите на команду\n/catalog",
                               reply_markup=markup)
    except:
        await message.reply(text="Чтобы можно было общаться с ботом, "
                                 "ты можешь написать мне в личные сообщение: "
                                 "https://t.me/arcanashop_dota2_bot")


# @dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=HELP_TEXT)


# @dp.message_handler(commands='description')
async def cmd_description(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Привет ✋, мы компания по продаже различных товаров!, "
                                "Мы очень рады что Вы используете"
                                "наш сервис ❤️, мы работает с Понедельника до "
                                "Пятницы.\n9:00 - 21:00")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=randrange(1, 100),
                            longitude=randrange(1, 100))


def default_handlers_register():
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_help, commands='help')
    dp.register_message_handler(cmd_description, commands='description')
