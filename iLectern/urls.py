from django.conf.urls import include, url
from django.contrib import admin
from sheets import urls as sheets_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sheets/', include(sheets_urls, namespace='sheets')),
    url(r'^', include(sheets_urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
