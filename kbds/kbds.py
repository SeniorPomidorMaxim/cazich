from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

row1 = [
    InlineKeyboardButton(
        text='⭐1WIN Mines Bot⭐',
        callback_data='1win_callback'
    )
]
rows1 = [row1]

markup1 = InlineKeyboardMarkup(inline_keyboard=rows1)


row2 = [
     InlineKeyboardButton(
        text='Continue',
        callback_data='continue_callback'
    )
]
row2 = [row2]

markup2 = InlineKeyboardMarkup(inline_keyboard=row2)



