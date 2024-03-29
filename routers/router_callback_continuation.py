from aiogram import Router, F, types
from aiogram.types import CallbackQuery

from kbds.kbds_countries import markup3
from routers.choose_countries import choose_countries

router_callback_continuation = Router()
router_callback_continuation.include_routers(choose_countries)
@router_callback_continuation.callback_query(F.data == 'continue_callback')
async def message_handler(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Where are you currently located?🌎",  reply_markup=markup3)