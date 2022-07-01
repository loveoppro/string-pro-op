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
        [InlineKeyboardButton("• sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ • ", callback_data="generate")],
        [
            InlineKeyboardButton("• ʜᴏᴡ ᴛᴏ ᴜsᴇ •", callback_data="help"),
            InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="about")
        ],
        [InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/OFFICIALHACKERERA")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/start - Start The Bot
/help - Help Message
/generate - Generate String Session
/cancel - Cancel The Process
/about - About Bot
"""

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Bot To Generate Pyrogram & Telethon String Sessions. 

Made With ❤ By @Mr_Agora and @Agora_Robots

Sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Agora_Robots)

Fʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

Lᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

Dᴇᴠᴇʟᴏᴘᴇʀ : [ΛႺՕ𝖱Λ](https://t.me/mr_agora)
    """
