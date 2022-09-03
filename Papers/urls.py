from django.urls import path

from . import views

app_name ='Papers'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/',views.viewCategory,name='viewCategory'),
    path('post/<int:post_id>/',views.viewPost,name='viewPost'),
    path('page/<int:page_id>/',views.viewPage,name='viewPage'),
    path('newPost/',views.newPost,name='newPost'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('updatePost/<int:post_id>', views.updatePost, name='updatePost'),
]
