from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from bots.group_controller_bot.views import (
    handle_telegram_webhook,
    set_telegram_webhook,
)

urlpatterns = [
    path("handle_telegram_webhook/", csrf_exempt(handle_telegram_webhook), name="telegram_webhook"),
    path("set/webhook/<str:token>/", set_telegram_webhook, name="set_telegram_webhook"),
]
