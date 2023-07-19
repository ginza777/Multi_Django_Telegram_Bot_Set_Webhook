import django.core.exceptions
import requests.exceptions
import telegram
from django.apps import AppConfig
from django.conf import settings


class BotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bots.bot4"

    def ready(self):
        try:
            bot_token = settings.BOT_TOKEN4
            webhook_url = settings.WEBHOOK_URL
            bot = telegram.Bot(token=bot_token)
            bot.set_webhook(f"{webhook_url}/bot4/handle_telegram_webhook/")
            print("Webhook set successfully for bot4: {}".format(bot.get_me().username))
        except telegram.error.RetryAfter:
            pass
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your internet connection")
        except django.core.exceptions.ImproperlyConfigured:
            print("Improperly configured. Please check your settings")
        except telegram.error.Unauthorized:
            print("Unauthorized. Please check your group_controller_bot token")
