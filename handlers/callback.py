from aiogram import types
from aiogram.dispatcher import FSMContext
from dispatcher import dp, db, bot
from configurator import config
import keyboard as kb

@dp.callback_query_handler()
async def callback_data(callback: types.CallbackQuery, state: FSMContext):
    if callback.message.chat.id == int(config.bot.chat_id) or callback.message.chat.id == int(config.bot.log_chat):
        if callback.data.startswith('back'):
            user_id = callback.data.split(':')[1]
            if callback.from_user.id == int(user_id):
                await callback.message.edit_text(f'Выберите', reply_markup=kb.menu(db.get_keyboard(), user_id=user_id))
            else:
                await callback.answer('⚠️ Не трогай пизды получишь!', show_alert=True)
            return
        elif callback.data.startswith('cancel'):
            user_id = callback.data.split(':')[1]
            if callback.from_user.id == int(user_id):
                await state.finish()
                await callback.message.edit_text('Успешно отменена!')
            else:
                await callback.answer('⚠️ Не трогай пизды получишь!', show_alert=True)
            return
        else:
            if callback.message.chat.id == int(config.bot.chat_id) or callback.message.chat.id == int(config.bot.log_chat):
                for i in db.get_callback_data_all():
                    if callback.data.startswith(i[2]):
                        user_id = callback.data.split(':')[1]
                        user_check = await bot.get_chat_member(callback.message.chat.id, callback.from_user.id)
                        if callback.from_user.id == int(user_id) or user_check.status == 'creator' or user_check.status == 'administrator' or callback.from_user.id == int(config.bot.owner):
                            await callback.message.edit_text(f'{i[3]}', reply_markup=kb.back(callback.from_user.id))
                        else:
                            await callback.answer('⚠️ Не трогай пизды получишь!', show_alert=True)
