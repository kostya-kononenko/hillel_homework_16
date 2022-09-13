from aggnew import views

from django.urls import path

app_name = 'aggnew'

urlpatterns = [path('', views.index, name='index'),
               path('publisher/', views.publisher, name='publisher'),
               path('publisher/<int:publisher_id>', views.publisher_book, name='publisher_book'),
               path('author/', views.author, name='author'),
               path('author/<int:young_author>', views.author_book, name='author_book'),
               path('books/', views.books, name='books'),
               path('books_all/', views.books_all, name='books_all'),
               path('books_one/<int:ids>', views.books_one, name='books_one'),
               path('store/', views.store, name='store'),
               path('store_books/<int:store_id>', views.store_books, name='store_books'),

               path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
               path('authors/', views.AuthorListView.as_view(), name='author-list'),
               path('authors/create', views.AuthorCreateView.as_view(), name='author-create'),
               path('authors/<int:pk>/update', views.AuthorUpdateView.as_view(), name='author-update'),
               path('authors/<int:pk>/delete', views.AuthorDeleteView.as_view(), name='author-delete'),

               ]
