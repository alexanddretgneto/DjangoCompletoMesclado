"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('menu', views.menu, name="menu"),
    path('book/', views.book, name="book"), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)