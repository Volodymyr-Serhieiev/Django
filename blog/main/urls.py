from django.urls import path
from .views import home_page, about, post, update_post, comment, create, delete

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blogs/', home_page, name='home_page'),
    path('about/', about),
    path('create/', create, name='create'),
    path('post/<slug:post_id>/', post, name='post'),
    path('<slug:slug>/comment/', comment),
    path('<slug:slug>/update/', update_post),
    path('<slug:slug>/delete/', delete),

]
