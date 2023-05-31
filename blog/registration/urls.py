from django.urls import path
from .views import profile, change_password, register, login, logout

urlpatterns = [
    path('profile/<str:username>/', profile),
    path('change_password/', change_password),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
]