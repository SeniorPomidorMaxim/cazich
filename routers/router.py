from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message



from kbds.kbds_language import markup_language

from routers.router_countries import router_callback

start_router = Router()
start_router.include_routers(router_callback)
@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text=f"""𝗪𝗲𝗹𝗰𝗼𝗺𝗲 {message.from_user.username}!

Choose a language for comfortable use of Game Hacks """,
        reply_markup=markup_language,
                    )
