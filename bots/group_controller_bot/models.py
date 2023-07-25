import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class LanguageChoice(models.TextChoices):
    UZBEK = "uz", _("O'zbekcha")
    KARAKALPAK = "kk", _("Qoraqolpoqcha")
    RUSSIAN = "ru", _("Ruscha")


class TelegramProfile(models.Model):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    language_code = models.CharField(max_length=255, choices=LanguageChoice.choices, null=True, blank=True)
    display_language = models.CharField(max_length=255, choices=LanguageChoice.choices, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_bot = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    extra_json = models.JSONField(null=True, blank=True)
    extra_text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username) or self.token or uuid.uuid4()
        super(TelegramProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.telegram_id}"

    class Meta:
        verbose_name = _("Telegram profile")
        verbose_name_plural = _("Telegram profiles")
        db_table = "GroupControllerBot_telegramprofile"


class TelegramProfileAdmin(models.Model):
    user = models.ForeignKey(TelegramProfile, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    extra_json = models.JSONField(null=True, blank=True)
    extra_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.user.username} {self.user.telegram_id}"


class MyGroups(models.Model):
    user = models.ForeignKey(TelegramProfile, on_delete=models.CASCADE)
    group_id = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255, null=True, blank=True)
    group_username = models.CharField(max_length=255, null=True, blank=True)
    group_type = models.CharField(max_length=255, null=True, blank=True)
    group_description = models.TextField(null=True, blank=True)
    group_image = models.ImageField(upload_to='images/', null=True, blank=True)
    group_link = models.CharField(max_length=255, null=True, blank=True)
    group_created_at = models.DateTimeField(auto_now_add=True)
    group_updated_at = models.DateTimeField(auto_now=True)
    group_extra_json = models.JSONField(null=True, blank=True)
    group_extra_text = models.TextField(null=True, blank=True)
    group_slug = models.SlugField(max_length=100, unique=True, blank=True)
    group_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.group_slug:
            self.group_slug = slugify(self.group_name) or self.group_uuid or uuid.uuid4()
        super(MyGroups, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.group_name} {self.group_username} {self.group_type} {self.group_link}"


class MyGroupMembers(models.Model):
    group = models.ForeignKey(MyGroups, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=255)
    member_name = models.CharField(max_length=255, null=True, blank=True)
    member_username = models.CharField(max_length=255, null=True, blank=True)
    member_type = models.CharField(max_length=255, null=True, blank=True)
    member_description = models.TextField(null=True, blank=True)
    member_image = models.ImageField(upload_to='images/', null=True, blank=True)
    member_created_at = models.DateTimeField(auto_now_add=True)
    member_updated_at = models.DateTimeField(auto_now=True)
    member_extra_json = models.JSONField(null=True, blank=True)
    member_extra_text = models.TextField(null=True, blank=True)
    member_slug = models.SlugField(max_length=100, unique=True, blank=True)
    member_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_bot = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False, null=True, blank=True)
    is_creator = models.BooleanField(default=False, null=True, blank=True)
    extra_json = models.JSONField(null=True, blank=True)
    extra_text = models.TextField(null=True, blank=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.member_slug:
            self.member_slug = slugify(self.member_name) or self.member_uuid or uuid.uuid4()
        super(MyGroupMembers, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.member_name} {self.member_username} {self.member_type} "


class GroupMemberInviteStatus(models.Model):
    group_member = models.ForeignKey(MyGroupMembers, on_delete=models.CASCADE)
    invite_status = models.ManyToManyField(MyGroupMembers, related_name='invite_status', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MyGroupAdmins(models.Model):
    user = models.ForeignKey(TelegramProfile, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(MyGroups, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.group}"


class MyGroupSettings(models.Model):
    send_ads_by_user = models.BooleanField(default=False)
    send_ads_by_admin = models.BooleanField(default=False)
    member_count = models.PositiveIntegerField(default=0)
    adding_user_count = models.PositiveIntegerField(default=0)
    group = models.ForeignKey(MyGroups, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.group) or self.uuid or uuid.uuid4()
        super(MyGroupSettings, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.group} {self.member_count} {self.adding_user_count} {self.send_ads_by_user} {self.send_ads_by_admin}"


class send_ads(models.Model):
    group = models.ManyToManyField(MyGroups)
    ads_id = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(TelegramProfile, on_delete=models.CASCADE)
    extra_json = models.JSONField(null=True, blank=True)
    extra_text = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ads_id) or self.uuid or uuid.uuid4()
        super(send_ads, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.ads_id} {self.slug} {self.uuid} {self.created_at} {self.updated_at} {self.user} {self.extra_json} {self.extra_text}"
