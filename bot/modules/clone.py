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
        msg = sendMessage(f"šš¹š¼š»š¶š»š“..šŖš®š¶š š½š¹š.š¤\n\nšØ Link:\n <code>{link}</code>",context.bot,update)
        gd = GoogleDriveHelper()
        result, button = gd.clone(link)
        deleteMessage(context.bot,msg)
        sendMarkup(result,context.bot,update,button)
    else:
         sendMessage("Dammnn šš \nProvide Google Drive Shareable Link For Clone š\n\nš¢ šš±šš¦š©š„š:\n <code>/clon1 your Google drive Link</code>\n\nš” For More Help Join Support Group\n šØ @MaxxBotChat",context.bot,update)

clone_handler = CommandHandler(BotCommands.CloneCommand,cloneNode,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(clone_handler)


from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.telegram_helper.message_utils import *
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.bot_utils import new_thread
from bot import dispatcher, LOGGER
 
 
@new_thread
def cloneNode(update,context):
    if update.message.from_user.last_name:
        last_name = f" {update.message.from_user.last_name}"
    else:
        last_name = ""
    if update.message.from_user.username:
        username = f"@{update.message.from_user.username}"
    else:
        username = ""
    name = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}{last_name}</a>'
 
    args = update.message.text.split(" ",maxsplit=1)
    if len(args) > 1:
        link = args[1]
        msg = f"<code>Cloning....</code>\n\n<b>Wait Little bit. š</b>\n\n" \
              f"<b>š¤ Upload by :</b> {username}\n\n" \
              f"<b>š Drive Link :</b> <code>{link}</code>"
        sendMessage(msg, context.bot, update)
        gd = GoogleDriveHelper()
        result, button = gd.clone(link)
        LOGGER.info('ID: {} - Username: {} - Message: {}'.format(update.message.chat.id,update.message.chat.username,update.message.text))
        # deleteMessage(context.bot,msg)
        sendMarkup(result,context.bot,update,button)
    else:
        sendMessage("Dammnn šš \nProvide Google Drive Shareable Link For Clone š\n\nš¢ šš±šš¦š©š„š:\n <code>/clon1 your Google drive Link</code>\n\nš” For More Help Join Support Group\n šØ @MaxxBotChat",context.bot,update)

clone_handler = CommandHandler(BotCommands.CloneCommand,cloneNode,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(clone_handler)
