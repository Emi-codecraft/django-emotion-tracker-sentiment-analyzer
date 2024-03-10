# project1/urls.py
from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('ebook/', include('ebook.urls')),
    path('sentimental_analysis/', include('sentimental_analysis.urls')),
    # Add other URL patterns for the project as needed
]
