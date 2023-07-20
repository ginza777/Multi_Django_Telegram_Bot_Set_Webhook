from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils.text import slugify
class LanguageChoice(models.TextChoices):
    UZBEK = "uz", _("O'zbekcha")
    KARAKALPAK = "kk", _("Qoraqolpoqcha")
    RUSSIAN = "ru", _("Ruscha")


class TelegramProfile(models.Model):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, choices=LanguageChoice.choices, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_bot = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    extra_json = models.JSONField(null=True, blank=True)
    extra_text = models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    token=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username) or self.token or uuid.uuid4()
        super(TelegramProfile, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.telegram_id}"
