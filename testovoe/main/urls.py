from django.urls import path
from main.views import url_redirect, url_shorter, home

app_name = 'main'

urlpatterns = [
    path('url_shorter/', url_shorter, name='url_shorter'),
    path('', home, name='home'),
    path('slug/<str:slug>/', url_redirect, name='url_redirect')
    ]
