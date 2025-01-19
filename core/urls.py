from django.urls import path

from .views import IndexListview

urlpatterns = [
    path('', IndexListview.as_view(), name='index'),
]
