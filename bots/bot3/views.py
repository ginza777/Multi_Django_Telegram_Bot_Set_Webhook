import json
import os
from queue import Queue

from django.conf import settings
from django.http import JsonResponse
from telegram import Bot, Update
from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    Dispatcher,
    Filters,
    MessageHandler,
    PicklePersistence,
)

from .state import state
from .telegrambot import get_language, start


def setup(token):
    bot = Bot(token=token)
    queue = Queue()
    # create the dispatcher
    if not os.path.exists(os.path.join(settings.BASE_DIR, "media", "state_record")):
        os.makedirs(os.path.join(settings.BASE_DIR, "media", "state_record"))
    dp = Dispatcher(
        bot,
        queue,
        workers=8,
        use_context=True,
        persistence=PicklePersistence(
            filename=os.path.join(settings.BASE_DIR, "media", "state_record", "conversationbot")
        ),
    )

    states = {
        state.MAIN: [
            MessageHandler(Filters.all, start),
        ],
        state.LANGUAGE: [
            CallbackQueryHandler(get_language),
        ],
    }
    entry_points = [CommandHandler("start", start)]
    fallbacks = [CommandHandler("start", start)]

    conversation_handler = ConversationHandler(
        entry_points=entry_points,
        states=states,
        fallbacks=fallbacks,
        persistent=True,
        name="conversationbot",
    )
    dp.add_handler(conversation_handler)
    return dp


def handle_telegram_webhook(request):
    token = settings.BOT_TOKEN3
    bot = Bot(token=token)
    update = Update.de_json(json.loads(request.body.decode("utf-8")), bot)
    dp = setup(token)
    try:
        if update.message.chat.type == "private":
            dp.process_update(update)
        else:
            if update.message.reply_to_message:
                dp.process_update(update)

    except Exception as e:
        dp.process_update(update)
    return JsonResponse({"status": "ok"})


def set_telegram_webhook(request):
    token = settings.BOT_TOKEN
    bot = Bot(token=token)
    bot.set_webhook(f"{settings.WEBHOOK_URL}/bot/handle_telegram_webhook/")
    return JsonResponse({"status": "ok"})
