import pyrogram

from plugins.help_text import rename_cb, cancel_extract
from plugins.rename_file import force_name


@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)
        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
       
    if query.data == "start_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚙️Help", callback_data="help_data"),
                    InlineKeyboardButton("About Me👨🏻‍🎓", callback_data="about_data")
                ],
                [
                    InlineKeyboardButton("BOT Channel📣", url="https://t.me/NeonBotZ"),
                    InlineKeyboardButton("Support Group💬", url="https://t.ME/NeonChatz")
                ]
            ]
        )

        await query.message.edit_text(
            Script.START_USER.format(query.from_user.mention),
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "help_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Channel📣", url="https://t.ME/NEONBOTZ"),
                    InlineKeyboardButton("About Me👨🏻‍🎓", callback_data="about_data")
                ]
            ]
        )

        await query.message.edit_text(
            Script.HELP_USER,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "about_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Channel📣", url="https://t.ME/NEONBOTZ"),
                    InlineKeyboardButton("⚙️Help", callback_data="help_data")
                ]
            ]
        )

        await query.message.edit_text(
            Script.ABOUT_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return
