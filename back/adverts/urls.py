from django.contrib import admin
from django.urls import path, include
from adverts import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', views.AdvertView)

urlpatterns = [
    path('', include(router.urls)),
    path('instrument', views.InstrumentView.as_view())
]
