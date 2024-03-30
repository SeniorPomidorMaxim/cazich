import asyncio
import logging
import sys


from app import dp, bot


async def main() -> None:
    await bot.delete_my_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())