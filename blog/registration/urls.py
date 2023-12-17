from django.urls import path
from .views import profile, change_password, registration, my_logout, my_login

urlpatterns = [
    path('profile/<str:username>/', profile),
    path('profile/<str:username>/', profile),
    path('change_password/', change_password),
    path('registration/', registration, name='registration'),
    path('login/', my_login, name='login'),
    path('logout/', my_logout, name='logout'),
]