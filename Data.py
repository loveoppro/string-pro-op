from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/OFFICIALHACKERERA) [!](https://te.legra.ph/file/4f730af88f1d7ec343386.jpg)"""

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
          InlineKeyboardButton("• ᴄʜᴀɴɴᴇʟ •", url="https://t.me/Broken_Heart73"),
          InlineKeyboardButton("• sᴜᴘᴘᴏʀᴛ •", url="https://t.me/HEPPYLIFI"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ  •", url="https://t.me/OFFICIALHACKERERA")
        ]
        ]



 
