from django.urls import path
from .views import Home, CreateAuthor

urlpatterns = [
    path('', Home, name='index'),
    path('create_author', CreateAuthor, name='create_author')
]