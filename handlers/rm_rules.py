from aiogram import types
from aiogram.dispatcher.filters import Text
from dispatcher import dp, db, bot
from configurator import config

@dp.message_handler(Text(startswith='-правила', ignore_case=True))
async def add_rul(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        user_check = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if user_check.status == 'creator' or user_check.status == 'administrator' or message.from_user.id == int(config.bot.owner):
            try:
                try:
                    btn_name = message.text[9:].split('\n')[0]
                except IndexError:
                    btn_name = message.text[9:].split('\n')[1]
            except:
                await message.answer('Неправильный аргумент!\n\nНапример:\n-правила [имя кнопки]')
                return
            check_btn = db.get_keyboard_name(btn_name)
            if not check_btn:
                await message.answer('⚠️ Произошло какая то ошибка проверьте название кнопки')
                return
            db.delete_rules(btn_name=btn_name)
            await message.answer(f'✅ Правила {btn_name} успешно удалена!')
