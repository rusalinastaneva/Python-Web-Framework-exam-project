from django.urls import path

from .views import index, AboutTemplateView

urlpatterns = [
    path('', index, name='index'),
    path('about', AboutTemplateView.as_view(), name='about'),
]