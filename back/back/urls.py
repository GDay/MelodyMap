from django.contrib import admin
from django.urls import path, include
from users import urls as user_urls
from adverts import urls as advert_urls
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.urls import re_path

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'^_nuxt/(?P<path>.*)$', RedirectView.as_view(url='/static/js/_nuxt/%(path)s', permanent=True)),
    path('sw.js', RedirectView.as_view(url='/static/js/_nuxt/sw.js', permanent=True)),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/auth/', include(user_urls)),
    path('api/adverts/', include(advert_urls))
]
