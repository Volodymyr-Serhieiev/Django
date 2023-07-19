from django.urls import path
from .views import profile, change_password, registration, login, logout

urlpatterns = [
    path('profile/<str:username>/', profile),
    path('change_password/', change_password),
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout),
]