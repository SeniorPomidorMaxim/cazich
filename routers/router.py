from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


from kbds.kbds import markup1
from routers.router_countries import router_callback

start_router = Router()
start_router.include_routers(router_callback)
@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text=f"""𝗪𝗲𝗹𝗰𝗼𝗺𝗲 {message.from_user.username}!

𝗦𝗲𝗹𝗲𝗰𝘁 𝘄𝗵𝗶𝗰𝗵 𝗠𝗶𝗻𝗲𝘀 𝗕𝗼𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝗿𝗲𝗰𝗲𝗶𝘃𝗲💎!""",
        reply_markup=markup1,
                    )