from django.urls import path
from .views import BooksListView, BooksAddView


urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/add/', BooksAddView.as_view(), name='books_add'),
]