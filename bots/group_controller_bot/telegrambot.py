import logging

from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _
from telegram import Update
from telegram.ext import CallbackContext

from .buttons.keyboard import main_buttons
from .models import LanguageChoice
from .state import state

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(str(_("Welcome our group_controller_bot")))
    return state.MAIN


def get_language(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    if data in LanguageChoice.values:
        activate(data)
        query.message.delete()
        query.message.reply_html(text=str(_("Welcome our group_controller_bot")), reply_markup=main_buttons())
        return state.MAIN
    return state.LANGUAGE


def main(update: Update, context: CallbackContext):
    try:
        context.bot.delete_message(chat_id=update.message.chat_id, message_id=context.user_data["message_id"])
    except Exception as e:
        pass
    return state.MAIN
