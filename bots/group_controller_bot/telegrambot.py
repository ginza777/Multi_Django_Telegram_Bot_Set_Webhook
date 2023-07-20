import logging
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _
from telegram import Update
from telegram.ext import CallbackContext

from bots.group_controller_bot.buttons.keyboard import main_buttons
from bots.group_controller_bot.models import LanguageChoice
from bots.group_controller_bot.state import state
from bots.group_controller_bot.buttons.inline import change_language_buttons

logger = logging.getLogger(__name__)


def main(update: Update, context: CallbackContext):
    try:
        print(update.message)

    except Exception as e:
        print(e)
    return state.MAIN


def start(update: Update, context: CallbackContext):
    update.message.reply_text(str(_("Welcome our group_controller_bot")))
    update.message.reply_html(text=str(_("Please choise your language: ")),
                              reply_markup=change_language_buttons())
    return state.LANGUAGE


def get_language(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    if data in LanguageChoice.values:
        activate(data)
        query.message.delete()
        query.message.reply_html(text=str(_("Buttons:")), reply_markup=main_buttons())
        return state.MAIN
    return state.LANGUAGE
