from django.utils.translation import gettext_lazy as _
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bots.group_controller_bot.models import LanguageChoice

#language
def change_language_buttons():
    languages = LanguageChoice.choices
    buttons = []
    for language in languages:
        buttons.append(
            [InlineKeyboardButton(text=str(_(language[1])), callback_data=language[0])],
        )
    return InlineKeyboardMarkup(buttons)


def back_inline_button():
    button = [[InlineKeyboardButton(str(_("Back")), callback_data="back")]]

    return InlineKeyboardMarkup(button)


def admin_main_buttons():
    buttons = [
        [
            InlineKeyboardButton(str(_("Add location")), callback_data="admin_location"),
        ]
    ]

    return InlineKeyboardMarkup(buttons)





# useful_information_buttons
# def useful_information_buttons():
#     buttons = [
#         [
#             InlineKeyboardButton(str(_("Links")), callback_data="links"),
#         ],
#         [
#             InlineKeyboardButton(str(_("Videos")), callback_data="videos"),
#         ],
#         [
#             InlineKeyboardButton(str(_("Infographics")), callback_data="infographics"),
#         ],
#         [
#             InlineKeyboardButton(str(_("Back")), callback_data="back"),
#         ],
#     ]
#
#     return InlineKeyboardMarkup(buttons)
