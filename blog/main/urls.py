from django.urls import path
from .views import home_page, about, post, update_post, comment, PostCreateView, delete, PostCreate

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about),
    path('create_post/', PostCreateView.as_view(), name='create-post'),
    path('post/<slug:slug>/', post, name='post'),
    path('posts-by-topic/<str:slug>/', home_page, name='posts-by-topic'),
    path('<slug:slug>/comment/', comment),
    path('<slug:slug>/update/', update_post),
    path('<slug:slug>/delete/', delete),

]
