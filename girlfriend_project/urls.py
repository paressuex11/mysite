from django.urls import path

from .views import dream, dream2

urlpatterns = [
    path('', dream),
    path('dream2/', dream2),
]