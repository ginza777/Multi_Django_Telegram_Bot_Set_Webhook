import django.core.exceptions
import requests.exceptions
import telegram
from django.apps import AppConfig
from django.conf import settings


class BotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bots.group_controller_bot"

    def ready(self):
        try:
            bot_token = settings.BOT_TOKEN
            webhook_url = settings.WEBHOOK_URL
            bot = telegram.Bot(token=bot_token)
            bot.set_webhook(f"{webhook_url}/group_controller_bot/handle_telegram_webhook/")
            print("=============================================================\n\n ")
            print("Webhook set successfully for group_controller_bot: {}".format(bot.get_me().username))
        except telegram.error.RetryAfter:
            pass
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your internet connection")
        except django.core.exceptions.ImproperlyConfigured:
            print("Improperly configured. Please check your settings")
        except telegram.error.Unauthorized:
            print("Unauthorized. Please check your group_controller_bot token")
