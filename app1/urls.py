from django.urls import path
from .views import set_cookie, get_cookie

urlpatterns = [
    path('set/', set_cookie),
    path('get/', get_cookie),
]
