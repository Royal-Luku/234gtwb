from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """
 𝙔𝙤𝙪 𝘾𝙖𝙣 𝘾𝙝𝙤𝙤𝙨𝙚 𝘼𝙣𝙮 𝙋𝙡𝙖𝙣 𝙬𝙝𝙖𝙩 𝙮𝙤𝙪 𝙡𝙞𝙠𝙚 ✌

𝟏.   𝙁𝙧𝙚𝙚 𝙋𝙡𝙖𝙣

•>    ᴅᴀɪʟʏ  ʟɪᴍɪᴛ 2 
•>    ꜰʀᴇᴇ

3.  𝘽𝙖𝙨𝙞𝙘 𝙋𝙡𝙖𝙣

•>     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  10 ɢʙ
•>     ʙᴜʏ  <a href='https://telegram.me/royaldwip'>₹ 30/ᴍᴏɴᴛʜ.</a> 
	
4.   𝙎𝙩𝙖𝙣𝙙𝙖𝙧𝙙 𝙋𝙡𝙖𝙣

•>     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  50 ɢʙ
•>     ʙᴜʏ  <a href='https://telegram.me/royaldwip'>₹ 60/ᴍᴏɴᴛʜ.</a>  
	

4.   𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝙋𝙡𝙖𝙣

•>     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  100 ɢʙ
•>     ʙᴜʏ  <a href='https://telegram.me/royaldwip'>₹ 110/ᴍᴏɴᴛʜ.</a>

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•
"""
	keybord = InlineKeyboardMarkup(
                [
                    [
            InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ  ᴛᴏ  ᴏᴡɴᴇʀ',url='https://telegram.me/royaldwip')
            ],
                    [
            InlineKeyboardButton('ᴏᴜʀ ᴀʟʟ ʙᴏᴛs',url='https://t.me/WOMBACKUP/47')
            ],
                    [
                        InlineKeyboardButton('ᴀʙᴏᴜᴛ ᴅᴇᴠ',url='https://t.me/About_Royaldwip'),
                        InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "cancel")
                    ]
                ]
            )
	await update.message.edit(text = text, disable_web_page_preview=True, reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """
𝙔𝙤𝙪 𝘾𝙖𝙣 𝘾𝙝𝙤𝙤𝙨𝙚 𝘼𝙣𝙮 𝙋𝙡𝙖𝙣 𝙬𝙝𝙖𝙩 𝙮𝙤𝙪 𝙡𝙞𝙠𝙚 ✌

𝟏.   𝙁𝙧𝙚𝙚 𝙋𝙡𝙖𝙣

•>    ᴅᴀɪʟʏ  ʟɪᴍɪᴛ 2 ɢʙ
•>    ꜰʀᴇᴇ

3.  𝘽𝙖𝙨𝙞𝙘 𝙋𝙡𝙖𝙣

•>     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  10 ɢʙ
•>     ʙᴜʏ  <a href='https://telegram.me/royaldwip'>₹ 30/ᴍᴏɴᴛʜ.</a> 
	
4.   𝙎𝙩𝙖𝙣𝙙𝙖𝙧𝙙 𝙋𝙡𝙖𝙣

•>     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  50 ɢʙ
•>     ʙᴜʏ  <a href='https://telegram.me/royaldwip'>₹ 60/ᴍᴏɴᴛʜ.</a>  
	

4.   𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝙋𝙡𝙖𝙣

•>     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  100 ɢʙ
•>     ʙᴜʏ  <a href='https://telegram.me/royaldwip'>₹ 110/ᴍᴏɴᴛʜ.</a>

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•
"""
	keybord = InlineKeyboardMarkup(
                [
                    [
            InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ  ᴛᴏ  ᴏᴡɴᴇʀ',url='https://telegram.me/royaldwip')
            ],
                    [
            InlineKeyboardButton('ᴏᴜʀ ᴀʟʟ ʙᴏᴛs',url='https://t.me/WOMBACKUP/47')
            ],
                    [
                        InlineKeyboardButton('ᴀʙᴏᴜᴛ ᴅᴇᴠ',url='https://t.me/About_Royaldwip'),
                        InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "cancel")
                    ]
                ]
            )
	await message.reply_text(text = text, disable_web_page_preview=True, reply_markup = keybord)
