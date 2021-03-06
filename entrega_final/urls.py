from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from AppCoder.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppCoder.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)