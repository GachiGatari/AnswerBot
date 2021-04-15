import configparser
import json
import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler

from KeyBoardobject import MainButton, ChildButton,MainKeyBoard

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read("settings.ini")
token = config["Telegram"]["token"]




def help_send(update: Update, _: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton(MainKeyBoard['counters'].text, callback_data=MainKeyBoard['counters'].callback),
            InlineKeyboardButton(MainKeyBoard['registration'].text, callback_data=MainKeyBoard['registration'].callback)
        ],
        [
            InlineKeyboardButton(MainKeyBoard['pay'].text, callback_data=MainKeyBoard['pay'].callback),
            InlineKeyboardButton(MainKeyBoard['other'].text, callback_data=MainKeyBoard['other'].callback)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Выберите один из вариантов:", reply_markup=reply_markup)


def button(update: Update, _: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data in MainKeyBoard.keys():
        query.edit_message_text(text="Выберите один из вариантов:", reply_markup=main_button(query.data))
    else:
        with open('answer.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        answer = data[query.data]
        query.edit_message_text(text=answer)


def main_button(callback) ->InlineKeyboardMarkup:
    keyboard = []
    for button in MainKeyBoard[callback].childs:
        keyboard.append([InlineKeyboardButton(button.text, callback_data=button.callback)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def main() -> None:
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('help', help_send))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
