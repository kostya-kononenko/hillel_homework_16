from agg import views

from django.urls import path

app_name = 'agg_store'

urlpatterns = [path('', views.index, name='index'),
               path('publisher/', views.publisher, name='publisher'),
               path('publisher/<int:publisher_id>', views.publisher_all_book, name='publisher_all_book'),
               path('books/', views.books, name='books'),
               path('books_list/', views.books_list, name='books_list'),
               path('books_detail/<int:ids>', views.books_detail, name='books_detail'),
               path('author/', views.author, name='author'),
               path('author/<int:min_author>', views.author_book_min, name='author_book_min'),
               path('author/<int:max_author>', views.author_book_max, name='author_book_max'),
               path('store/', views.store, name='store'),
               path('store_books/<int:store_id>', views.store_books, name='store_books'),
               ]
