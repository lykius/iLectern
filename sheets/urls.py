from django.conf.urls import include, url
from .views import (SheetListView, SheetView)

urlpatterns = [
    url(r'^$', SheetListView.as_view(), name='list'),
    url(r'^view/(?P<pk>[0-9]+)/$', SheetView.as_view(), name='view'),
]
