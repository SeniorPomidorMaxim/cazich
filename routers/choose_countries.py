from aiogram import Router, F, types
from aiogram.types import CallbackQuery

from kbds.kbds_choose import markup_choose
from routers.instruction_callback import instruction_callback

choose_countries = Router()
choose_countries.include_routers(instruction_callback)
@choose_countries.callback_query(F.data == 'europe_callback')
async def message_handler1(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer_photo(photo=types.FSInputFile('photo_test.jpeg'))
    await callback_query.message.answer("""Rules are simple:

1. Register in 1WIN account using my link ( button on link bellow, make at least a 10-20€ Deposit)

2. If you try to avoid my Stake link or google it, you will not be able to get 1WIN MINES BOT!🤖

3. After successful registration and deposit send a screenshot to #""", reply_markup=markup_choose)


@choose_countries.callback_query(F.data == 'north_america_callback')
async def message_handler2(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer_photo(photo=types.FSInputFile('photo_test.jpeg'))
    await callback_query.message.answer("""Rules are simple:

1. Register in 1WIN account using my link ( button on link bellow, make at least a 5-10$ Deposit)

2. If you try to avoid my Stake link or google it, you will not be able to get 1WIN MINES BOT!🤖

3. After successful registration and deposit send a screenshot to #""", reply_markup=markup_choose)


@choose_countries.callback_query(F.data == 'india_callback')
async def message_handler3(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer_photo(photo=types.FSInputFile('photo_test.jpeg'))
    await callback_query.message.answer("""Rules are simple:

1. Register in 1WIN account using my link ( button on link bellow, make at least a 700-1000₹ Deposit)

2. If you try to avoid my Stake link or google it, you will not be able to get 1WIN MINES BOT!🤖

3. After successful registration and deposit send a screenshot to #""", reply_markup=markup_choose)


@choose_countries.callback_query(F.data == 'turkey_callback')
async def message_handler4(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer_photo(photo=types.FSInputFile('photo_test.jpeg'))
    await callback_query.message.answer("""
Rules are simple:

1. Register in 1WIN account using my link ( button on link bellow, make at least a 500-1000₺ Deposit)

2. If you try to avoid my Stake link or google it, you will not be able to get 1WIN MINES BOT!🤖

3. After successful registration and deposit send a screenshot to #""", reply_markup=markup_choose)


@choose_countries.callback_query(F.data == 'africa_callback')
async def message_handler5(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer_photo(photo=types.FSInputFile('photo_test.jpeg'))
    await callback_query.message.answer("""Rules are simple:

1. Register in 1WIN account using my link ( button on link bellow, make at least a 5-10$ Deposit)

2. If you try to avoid my Stake link or google it, you will not be able to get 1WIN MINES BOT!🤖

3. After successful registration and deposit send a screenshot to #""", reply_markup=markup_choose)


@choose_countries.callback_query(F.data == 'other_callback')
async def message_handler6(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer_photo(photo=types.FSInputFile('photo_test.jpeg'))
    await callback_query.message.answer("""
Rules are simple:

1. Register in 1WIN account using my link ( button on link bellow, make at least a 5-10$ Deposit)

2. If you try to avoid my Stake link or google it, you will not be able to get 1WIN MINES BOT!🤖

3. After successful registration and deposit send a screenshot to#""", reply_markup=markup_choose)