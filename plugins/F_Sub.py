"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import FORCE_SUB


@Client.on_message(filters.private)
async def is_not_subscribed(client, message):
    if not client.force_channel:
        pass
    try:             
        user = await client.get_chat_member(client.force_channel, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:                       
             return await client.send_message(message.from_user.id, text="ππΎππ π°ππ΄ π±π°π½π½π΄π³ ππΎ πππ΄ πΌπ΄") 
        else:
             pass             
    except UserNotParticipant:               
        buttons = [[ InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=f"https://t.me/{FORCE_SUB}") ]]
        text = "**ππΎπππ π³ππ³π΄ ππΎππ π½πΎπ πΉπΎπΈπ½π³ πΌπ π²π·π°π½π½π΄π» π. πΏπ»π΄π°ππ΄ πΉπΎπΈπ½ πΌπ π²π·π°π½π½π΄π» ππΎ πππ΄ ππ·πΈπ π±πΎπ π **"
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



