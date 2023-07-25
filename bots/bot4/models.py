from django.db import models
from django.utils.translation import gettext_lazy as _


class LanguageChoice(models.TextChoices):
    UZBEK = "uz", _("O'zbekcha")
    KARAKALPAK = "kk", _("Qoraqolpoqcha")
    RUSSIAN = "ru", _("Ruscha")

#
# class TelegramProfile(models.Model):
#     telegram_id = models.PositiveBigIntegerField(unique=True)
#     first_name = models.CharField(max_length=255, null=True)
#     last_name = models.CharField(max_length=255, null=True, blank=True)
#     username = models.CharField(max_length=255, null=True, blank=True)
#     language = models.CharField(max_length=255, choices=LanguageChoice.choices, null=True, blank=True)
#     full_name = models.CharField(max_length=255, null=True, blank=True)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     is_admin = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} {self.username} {self.telegram_id}"
