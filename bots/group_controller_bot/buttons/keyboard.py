from django.utils.translation import gettext_lazy as _
from telegram import KeyboardButton, ReplyKeyboardMarkup


def main_buttons():
    return ReplyKeyboardMarkup(
        [

            [str(_("My Groups")), str(_("My Profile"))],
            [str(_("Useful information"))],
            [str(_("Settings"))],
            [str(_("Bot news")),str(_("About us"))],
        ]
    )


def my_groups_buttons():
    return ReplyKeyboardMarkup(
        [
        [str(_("Main menu"))],
         [str(_("My Groups info"))],
         [str(_("Send ads"))],
         [str(_("Main menu"))],

         ]
    )




def request_phone_button():
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(
                    text=str(_("📞Telefon raqamni yuborish")),
                    request_contact=True,
                    one_time_keyboard=True,
                )
            ]
        ],
        resize_keyboard=True,
    )


def request_location_button():
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(
                    text=str(_("📍Manzilni yuborish")),
                    request_location=True,
                    one_time_keyboard=True,
                )
            ]
        ],
        resize_keyboard=True,
    )

def add_group_button():
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(
                    text=str(_("Add group")),
                    one_time_keyboard=True,
                )
            ]
        ],
        resize_keyboard=True,
    )


def back_button():
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=str(_("⬅️Orqaga")))]],
        resize_keyboard=True,
    )
