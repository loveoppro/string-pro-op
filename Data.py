from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}, 
Welcome to {}
[➼](https://te.legra.ph/file/4f730af88f1d7ec343386.jpg)ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴏᴘᴇʀᴀᴛᴇ"""

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("• sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ •", callback_data="generate")],
        [InlineKeyboardButton(text="• ʜᴏᴍᴇ •", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("• sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ • ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [
         InlineKeyboardButton("• sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ • ", callback_data="generate"),
        
        ],
        [
            InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/OFFICIALHACKERERA")
           
        ]
    ]



 
