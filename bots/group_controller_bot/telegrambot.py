import logging

from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _
from telegram import Update
from telegram.ext import CallbackContext

from bots.group_controller_bot.buttons.inline import *
from bots.group_controller_bot.buttons.keyboard import *
from bots.group_controller_bot.functions import create_or_check_user
from bots.group_controller_bot.models import TelegramProfile, MyGroups
from bots.group_controller_bot.state import state

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
    message = create_or_check_user(update.effective_user)

    return state.LANGUAGE


def get_language(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    user = TelegramProfile.objects.get(telegram_id=update.effective_user.id)
    user.display_language = data
    user.save()
    activate(data)
    query.delete_message()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(
            _(f"Salom {user.username}!\n✅ Guruhga odam qo'shganlarni sanayman\n✅ Reklama\n✅ Guruhlar statistikasini\n✅ Majburiy odam qo'shtiraman\n\nQuyidagi tugmalar orqali  bot imkoniyatlaridan foydalanishingiz mumkin:")),
        reply_markup=main_buttons())
    return state.ADMIN_PANEL


def admin_panel(update: Update, context: CallbackContext):
    command_text=update.message.text
    user=TelegramProfile.objects.get(telegram_id=update.effective_user.id)
    if command_text==str(_("My Groups")):
        MyGroups.objects.filter(user=user)
        if MyGroups.objects.filter(user=user).exists():
            my_groups=MyGroups.objects.filter(user=user)
            for group in my_groups:
                update.message.reply_text(str(group.group_name))

            return state.ADMIN_PANEL
        else:
            update.message.reply_text(str(_("You don't have any groups !")))
            update.message.reply_text(str(_("Please add your group\n send your group id or link ")),reply_markup=add_group_button())
            return state.ADD_GROUP
    if command_text==str(_("My Profile")):
        pass
    if command_text==str(_("Useful information")):
        pass
    if command_text==str(_("Settings")):
        pass
    if command_text==str(_("Bot news")):
        pass
    if command_text==str(_("About us")):
        pass
