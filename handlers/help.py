from aiogram.dispatcher.filters import Text
from dispatcher import dp, bot, db
from aiogram import types
import keyboard as kb
from configurator import config

@dp.message_handler(Text('правила', ignore_case=True))
async def rules_cmd(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        if not db.check_db():
            await message.answer('📝 Правила чата пока не заданы.')
            return
        if message.reply_to_message:
            await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.reply_to_message.from_user.id))
            return
        await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.from_user.id))


@dp.message_handler(Text('!правила', ignore_case=True))
async def rules_cmd(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        if not db.check_db():
            await message.answer('📝 Правила чата пока не заданы.')
            return
        if message.reply_to_message:
            await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.reply_to_message.from_user.id))
            return
        await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.from_user.id))


@dp.message_handler(Text('пантера правила', ignore_case=True))
async def rules_cmd(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        if not db.check_db():
            await message.answer('📝 Правила чата пока не заданы.')
            return
        if message.reply_to_message:
            await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.reply_to_message.from_user.id))
            return
        await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.from_user.id))


@dp.message_handler(Text('!пантера правила', ignore_case=True))
async def rules_cmd(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        if not db.check_db():
            await message.answer('📝 Правила чата пока не заданы.')
            return
        if message.reply_to_message:
            await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.reply_to_message.from_user.id))
            return
        await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.from_user.id))




@dp.message_handler(Text('пантера покажи', ignore_case=True))
async def rules_cmd(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        if not db.check_db():
            await message.answer('📝 Правила чата пока не заданы.')
            return
        if message.reply_to_message:
            await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.reply_to_message.from_user.id))
            return
        await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.from_user.id))


@dp.message_handler(Text('!пантера покажи', ignore_case=True))
async def rules_cmd(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        if not db.check_db():
            await message.answer('📝 Правила чата пока не заданы.')
            return
        if message.reply_to_message:
            await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.reply_to_message.from_user.id))
            return
        await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.from_user.id))


@dp.message_handler(Text('!пр', ignore_case=True))
async def rules_cmd(message: types.Message):
    if message.chat.id == int(config.bot.chat_id) or message.chat.id == int(config.bot.log_chat):
        if not db.check_db():
            await message.answer('📝 Правила чата пока не заданы.')
            return
        if message.reply_to_message:
            await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.reply_to_message.from_user.id))
            return
        await bot.send_message(message.chat.id, 'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=message.from_user.id))

