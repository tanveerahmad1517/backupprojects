from django.conf.urls import url
from .import views
# from posts.views import HomeView
from django.urls import path
from account.views import profile

app_name = 'posts'
urlpatterns = [
    path('', views.AllPostList.as_view(), name="all"),
    # path('posts/', views.posts, name='all'),
    path('<int:pk>/', views.post_detail, name="detail"),
    path('create/', views.new_post, name="post_create"),
    path('<int:pk>/edit/', views.edit_post, name="post_edit"),
    path('<int:pk>/delete/', views.PostDeletePost.as_view(), name="post_delete"),

    
    
    
    

]