from aiogram import Router, F, types
from aiogram.types import CallbackQuery

instruction_callback = Router()
@instruction_callback.callback_query(F.data == 'restricted_callback')
async def message_handler(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Here is tutorial for those if access to bookmaker is restricted:")
    await callback_query.message.answer_video(video=types.FSInputFile('settings_vpn.mp4'))
    await callback_query.message.answer("""First you download any VPN and (turn on 𝗔𝗿𝗴𝗲𝗻𝘁𝗶𝗻𝗮🇦🇷)

Then find your country code at 1WIN!
Check Video⬆️""")



@instruction_callback.callback_query(F.data == 'instruction_callback')
async def message_handler(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("""The bot is based on and trained using OpenAI's neural network cluster 🖥[ChatGPT-v4].

For training, the bot played 🎰 over 8000 games.
Currently, bot users successfully make 20-30% of their 💸capital daily!

The bot is still learning, and its accuracy
is at 85%!

Follow these instructions for maximum profit:


🔸 1. Register at the 1WIN betting office.If it doesn’t open - use a VPN (Norway).I use VPN Super Unlimited Proxy
Access to signals will not be available without registration!

🔸 2. Deposit funds into your account.

🔸 3. Go to the 1win games section and select the 💣"MINES" game.

🔸 4. Set the number of traps to three. This is important!

🔸 5. Request a signal from the bot and place bets based on the bot’s signals.

🔸 6. In case of a losing signal, we advise you to double (X2) your bet to fully cover the loss in the next signal.""")