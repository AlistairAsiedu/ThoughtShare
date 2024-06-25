from django.urls import path
from . import views

# Url patterns mapped to the different views
urlpatterns = [
    path('', views.Thoughtshare),
    path('welcome/', views.welcome, name='welcome'),
    path('list', views.list, name='list'),
    path('add/', views.add_post, name='add_post'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
