import random
from aiogram import types
from aiogram.dispatcher.filters import Text
from dispatcher import dp, db, bot
from configurator import config


@dp.message_handler(Text(startswith='+правила', ignore_case=True))
async def add_rul(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        user_check = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if user_check.status == 'creator' or user_check.status == 'administrator' or message.from_user.id == int(config.bot.owner):
            try:
                try:
                    text = message.text.split('\n')[1:]
                    btn_name = message.text[9:].split('\n')[0]
                except IndexError:
                    text = message.text.split('\n')[0:]
                    btn_name = message.text[9:].split('\n')[1]
            except:
                await message.answer('Неправильный аргумент!\n\nНапример:\n+правила [имя кнопки]\nС новой строки [правила]')
                return
            text = "\n".join(text)
            randomize = random.randint(111111, 9999999)
            check_callback = db.get_callback_data(id_or_name=f'kb_{randomize}')
            check_btn = db.get_keyboard_name(id_or_name=btn_name)
            if not check_callback and not check_btn:
                db.insert_rule(btn_name=btn_name, callback_data=f'kb_{randomize}', rules=text)
                await message.answer('✅ Правила успешно добавлено!')
            else:
                await message.answer('⚠️ Произошло какая то ошибка проверьте и повторите попытку')
