from django.urls import path
from .views import home_page, about, post, update_post, comment, create, delete

urlpatterns = [
    path('blogs/', home_page),
    path('/', home_page),
    path('', home_page),
    path('about/', about),
    path('create/', create),
    path('<slug:slug>/', post),
    path('<slug:slug>/comment/', comment),
    path('<slug:slug>/update/', update_post),
    path('<slug:slug>/delete/', delete),

]
