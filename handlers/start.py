from aiogram import types
from dispatcher import bot, dp
from configurator import config


@dp.message_handler(commands=['db'])
@dp.edited_message_handler(commands=['db'])
async def db_cmd(message: types.Message):
    if message.from_user.id == int(config.bot.owner):
        try:
            await bot.send_document(chat_id=message.chat.id, document=open(file='db.db', mode='rb'))
        except:
            await message.reply(f'Ошибка')
            return
    else:
        await bot.send_message(message.chat.id, f'У вас нет доступа')
