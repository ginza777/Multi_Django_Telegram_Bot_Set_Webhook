from .models import TelegramProfile


def create_or_check_user(tg_user):
    print(tg_user)
    try:
        user=TelegramProfile.objects.get(telegram_id=tg_user['id'])
        user.username=tg_user['username']
        user.first_name=tg_user['first_name']
        user.last_name=tg_user['last_name']
        user.language_code=tg_user['language_code']
        user.is_bot=tg_user['is_bot']
        user.save()
        return print("user exists")

    except TelegramProfile.DoesNotExist:
        user=TelegramProfile.objects.create(
            telegram_id=tg_user['id'],
            first_name=tg_user['first_name'],
            last_name=tg_user['last_name'],
            username=tg_user['username'],
            language_code=tg_user['language_code'],
            is_active=True,
            is_bot=tg_user['is_bot'],

        )
        user.save()
        return print("user created")


