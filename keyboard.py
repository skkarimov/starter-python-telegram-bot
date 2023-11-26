from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def menu(db, user_id):
    btn = InlineKeyboardMarkup(row_width=2)
    for i in db:
        btn.insert(InlineKeyboardButton(text=f'{i[1]}', callback_data=f'{i[2]}:{user_id}'))
    return btn


def back(user_id):
    btn = InlineKeyboardMarkup()
    btn.add(InlineKeyboardButton(text=f'◀️ Назад', callback_data=f'back:{user_id}'))
    return btn


def cancel_btn(user_id):
    btn = InlineKeyboardMarkup()
    btn.add(InlineKeyboardButton(text=f'❌ Отмена', callback_data=f'cancel:{user_id}'))
    return btn


def settings_btn():
    btn = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text='Добавить правила', callback_data='add_rules')
    btn2 = InlineKeyboardButton(text='Удалить правила', callback_data='rm_rules')
    btn3 = InlineKeyboardButton(text='Изменить правила', callback_data='edit_rules')
    btn.add(btn1, btn2)
    btn.add(btn3)
    return btn
