from django.utils.translation import gettext_lazy as _
from telegram import KeyboardButton, ReplyKeyboardMarkup


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


def back_button():
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=str(_("⬅️Orqaga")))]],
        resize_keyboard=True,
    )


def main_buttons():
    return ReplyKeyboardMarkup(
        [
            [str(_("Election Stations"))],
            [str(_("F.A.Q"))],
            [str(_("Send an appeal"))],
            [str(_("Change language"))],
            [
                str(_("Useful information")),
            ],
        ]
    )
