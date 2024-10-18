# bookapp/urls.py

from django.urls import path     
from . import views 


urlpatterns = [
    path('createbook/', views.createBook, name='createbook'),
    path('createauthor/', views.createAuthor, name='author'),
    path('',views.listBook, name='booklist'),
    path('detailsview/<int:book_id>/',views.detailsView, name='details'),
    path('updateview/<int:book_id>/',views.updateBook,name='update'),
    path('deleteview/<int:book_id>/',views.deleteView,name='delete'),
    path('index',views.index),
    path('search/',views.searchBook, name='search')
    ] 


















