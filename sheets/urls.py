from django.conf.urls import include, url
from .views import (SheetListView, SheetView, SheetFormView)

urlpatterns = [
    url(r'^$', SheetListView.as_view(), name='list'),
    url(r'^view/(?P<pk>[0-9]+)/$', SheetView.as_view(), name='view'),
    url(r'^add/$', SheetFormView.as_view(), name='add')
]
