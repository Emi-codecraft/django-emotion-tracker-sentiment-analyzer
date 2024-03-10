# sentimental_analysis/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.sentimental_home, name='sentimental_home'),
    path('analyze/', views.analyze_sentiment, name='analyze_sentiment'),
]
