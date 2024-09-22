from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls',namespace='accounts')),
    path('dashboard/',include('dashboard.urls',namespace='dashboard')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
