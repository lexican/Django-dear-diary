
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.PostCreateView.as_view(template_name='create.html'), name='create'),
    path('post/<pk>/update/', views.PostUpdateView.as_view(template_name='post_update.html'), name='update-post'),
    path('post/<pk>/delete/', views.PostDeleteView.as_view(template_name='post_confirm_delete.html'), name='delete-post'),
]