from django.urls import path
from .views import ebook_home  # Make sure to import your view function

urlpatterns = [
    path('', ebook_home, name='ebook_home'),
    # Add other paths as needed
]
