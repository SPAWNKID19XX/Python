from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5466046553:AAE9haUA28enlGfpVqutAwkESJBbsQ5cAUg", use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello, I'm Spawnkid2022__bot, nice to meet you, how can i hel you")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL""")

def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://mail.google.com/mail/u/0/#inbox")

def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.linkedin.com/in/boris-isac-b11a601a6/")

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands
    
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()