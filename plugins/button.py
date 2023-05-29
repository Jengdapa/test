# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_GROUP2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:

        buttons = [

            [

                InlineKeyboardButton(text="GROUP2", url=client.invitelink3),

            ],

            [

                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),

                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),

            ],

        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="GROUP", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="CHANNEL", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="CHANNEL", url=client.invitelink),
                InlineKeyboardButton(text="GROUP", url=client.invitelink2),
                InlineKeyboardButton(text="GROUP2", url=client.invitelink3),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons

def fsub_button(client, message):

    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:

        buttons = [

            [

                InlineKeyboardButton(text="join group2", url=client.invitelink3),

            ],

        ]

        try:

            buttons.append(

                [

                    InlineKeyboardButton(

                        text="coba lagi",

                        url=f"https://t.me/{client.username}?start={message.command[1]}",

                    )

                ]

            )

        except IndexError:

            pass
        return buttons
def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="join group", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="join channel", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="join channel", url=client.invitelink),
                InlineKeyboardButton(text="join group", url=client.invitelink2),
                InlineKeyboardButton(text="join group2", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
