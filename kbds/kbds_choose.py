from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline1 = InlineKeyboardButton(
        text='REGISTER HERE🤑',
        url='https://web.telegram.org/a/#317046129'
    )

inline2 = InlineKeyboardButton(
        text='Restricted? Click here🪲',
        callback_data='restricted_callback'
    )

inline3 = InlineKeyboardButton(
        text='Instruction📖',
        callback_data='instruction_callback'
    )


row1 = [inline1]
row2 = [inline2]
row3 = [inline3]

rows = [
    row1,
    row2,
    row3,
]
markup_choose = InlineKeyboardMarkup(inline_keyboard=rows)