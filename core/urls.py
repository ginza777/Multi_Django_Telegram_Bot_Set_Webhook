from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .schema import swagger_urlpatterns


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("group_controller_bot/", include("bots.group_controller_bot.urls")),
    # custom bots---------------------------------------
    path("bot2/", include("bots.bot2.urls")),
    path("bot3/", include("bots.bot3.urls")),
    path("bot4/", include("bots.bot4.urls")),
    # --------------------------------------------------
    path("rosetta/", include("rosetta.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("sentry-debug/", trigger_error),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
