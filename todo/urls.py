# urls.py
from django.urls import path
from .views import read_books,read_list,BookUpdateView,BookDeleteView,home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', read_books, name='read_books'),  
    path('list',read_list,name='read_list'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
