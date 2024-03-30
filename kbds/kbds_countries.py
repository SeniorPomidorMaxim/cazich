from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline1 = InlineKeyboardButton(
        text='Europe🟥',
        callback_data='europe_callback'
    )

inline2 = InlineKeyboardButton(
        text='North America🟩',
        callback_data='north_america_callback'
    )

inline3 = InlineKeyboardButton(
        text='India🟪',
        callback_data='india_callback'
    )

inline4 = InlineKeyboardButton(
        text='Turkey🟨',
        callback_data='turkey_callback'
    )

inline5 = InlineKeyboardButton(
        text='Africa🟦',
        callback_data='africa_callback'
    )

inline6 = InlineKeyboardButton(
        text='Other🟧',
        callback_data='other_callback'
    )

row1 = [inline1]
row2 = [inline2]
row3 = [inline3]
row4 = [inline4]
row5 = [inline5]
row6 = [inline6]
rows = [
    row1,
    row2,
    row3,
    row4,
    row5,
    row6
]
markup3 = InlineKeyboardMarkup(inline_keyboard=rows)