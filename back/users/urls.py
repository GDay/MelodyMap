from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('logout', views.LogoutView.as_view()),
    path('login', views.LoginView.as_view()),
    path('signup', views.SignupView.as_view()),
    path('user', views.UserView.as_view()),
    path('CSRFtoken', views.CSRFTokenView.as_view())
]
