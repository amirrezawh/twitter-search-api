from django.contrib import admin
from django.urls import path, include
from . import settings

app_name = "twitter"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('twitter.urls',
    namespace="twitter-url")),
]
