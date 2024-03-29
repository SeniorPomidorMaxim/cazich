from aiogram import Router, F, types
from aiogram.types import CallbackQuery

from kbds.kbds import markup2
from routers.router_callback_continuation import router_callback_continuation

router_callback = Router()
router_callback.include_routers(router_callback_continuation)


@router_callback.callback_query(F.data == '1win_callback')
async def message_handler(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer_video(video=types.FSInputFile('video1win.mp4'))
    await callback_query.message.answer("Here how it's works⬆️", reply_markup=markup2)

