from django.urls import path
from .views import get_equity

urlpatterns = [
    path('equity', get_equity, name="equity"),
]
