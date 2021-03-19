from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.telegram_helper.message_utils import *
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.bot_utils import new_thread
from bot import dispatcher


@new_thread
def cloneNode(update,context):
    args = update.message.text.split(" ",maxsplit=1)
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"𝗖𝗹𝗼𝗻𝗶𝗻𝗴..𝗪𝗮𝗶𝘁 𝗽𝗹𝘀.🤓\n\n📨 Link:\n <code>{link}</code>",context.bot,update)
        gd = GoogleDriveHelper()
        result, button = gd.clone(link)
        deleteMessage(context.bot,msg)
        sendMarkup(result,context.bot,update,button)
    else:
         sendMessage("Dammnn 😒😐 \nProvide Google Drive Shareable Link For Clone 🌝\n\n📢 𝐄𝐱𝐚𝐦𝐩𝐥𝐞:\n <code>/clon1 your Google drive Link</code>\n\n💡 For More Help Join Support Group\n 📨 @MaxxBotChat",context.bot,update)

clone_handler = CommandHandler(BotCommands.CloneCommand,cloneNode,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(clone_handler)
