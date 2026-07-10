from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest
from database.users_chats_db import db
from info import ADMINS,MAX_SUBSCRIPTION_TIME,LAZYCONTAINER
from utils import temp,to_small_caps,lazy_readable
from datetime import datetime, timedelta
import pytz
import logging
import asyncio
from Script import script
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import get_file_details
from database.users_chats_db import db
from info import *
#5 => verification_steps ! [Youtube@LazyDeveloperr]
from utils import  get_size, temp
from urllib.parse import quote
from utils import schedule_deletion, to_small_caps
from plugins.commands import send_lazy_video
import base64
logger = logging.getLogger(__name__)
from utils import temp
import pytz  # Make sure to handle timezone correctly

timezone = pytz.timezone("Asia/Kolkata")

@Client.on_chat_join_request(filters.chat(AUTH_CHANNEL))
async def join_reqs(client, message: ChatJoinRequest):
  if not await db.find_join_req(message.from_user.id, message.chat.id):
    await db.add_join_req(message.from_user.id, message.chat.id)

@Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMINS))
async def del_requests(client, message):
    await db.del_join_req()   
    await message.reply("<b>⚙ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ᴄʜᴀɴɴᴇʟ ʟᴇғᴛ ᴜꜱᴇʀꜱ ᴅᴇʟᴇᴛᴇᴅ</b>")

# lazydeloper

# @Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMINS))
# async def del_requests(client, message):
#     await db.del_join_req()    
#     await message.reply("<b>⚙ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ᴄʜᴀɴɴᴇʟ ʟᴇғᴛ ᴜꜱᴇʀꜱ ᴅᴇʟᴇᴛᴇᴅ</b>")
