from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language1 = InlineKeyboardButton(
        text='🐫العربية',
        callback_data='arabic_language'
    )

language2 = InlineKeyboardButton(
        text='English🦁',
        callback_data='english_language'
    )

language3 = InlineKeyboardButton(
        text='भारतीय🐯',
        callback_data='india_language'
    )

language4 = InlineKeyboardButton(
        text='Türk🐺',
        callback_data='turkey_language'
    )

language5 = InlineKeyboardButton(
        text='Africa🦒',
        callback_data='africa_callback'
    )




row1 = [language1]
row2 = [language2]
row3 = [language3]
row4 = [language4]
row5 = [language5]

rows_language = [
    row1,
    row2,
    row3,
    row4,
    row5,
]
markup_language = InlineKeyboardMarkup(inline_keyboard=rows_language)