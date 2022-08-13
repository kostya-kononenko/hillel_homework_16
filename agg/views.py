from agg.models import Author, Book, Publisher, Store

from django.db.models import Avg, Count, Min, Max
from django.shortcuts import render


def index(request):
    return render(request, "agg/index.html")


def publisher(request):
    publisher_all = Publisher.objects.count()
    publisher_select = Book.objects.select_related('publisher')

    return render(
        request,
        "agg/publisher.html",
        {
            'pub_all': publisher_all,
            'pub_select': publisher_select,
         }
    )


def publisher_all_book(request, publisher_id):
    publisher_info = Book.objects.select_related('publisher')
    publisher_count_book = publisher_info.filter(publisher_id=publisher_id).count()
    publisher_books = publisher_info.filter(publisher_id=publisher_id)

    return render(
        request,
        "agg/publisher_book.html",
        {'pub_books': publisher_books,
         'count_book': publisher_count_book
         }
    )


def books(request):
    book = Book.objects.count()
    all_books = Book.objects.count()
    avg_price_book = Book.objects.all().aggregate(Avg('price'))
    max_price_book = Book.objects.all().aggregate(Max('price'))
    min_price_book = Book.objects.all().aggregate(Min('price'))

    return render(
        request,
        "agg/books.html",
        {'book': book,
         'all_book': all_books,
         'avg_price': avg_price_book['price__avg'],
         'max_price': max_price_book['price__max'],
         'min_price': min_price_book['price__min'],
         }
    )


def books_list(request):
    book_list = Book.objects.all()
    return render(
        request,
        "agg/books_list.html",
        {"books": book_list,
         }
                )


def books_detail(request, ids):
    book_authors = Book.objects.prefetch_related('authors')
    books_id = []
    books_name = []
    books_author = []
    books_price = []
    books_pages = []
    books_rating = []
    books_pubdate = []
    books_publisher = []
    for book in book_authors:
        authors = [author_book.name for author_book in book.authors.all()]
        if book.id == ids:
            books_id.append(book.id)
            books_name.append(book.name)
            books_author.append(authors)
            books_price.append(book.price)
            books_pages.append(book.pages)
            books_rating.append(book.rating)
            books_pubdate.append(book.pubdate)
            books_publisher.append(book.publisher)

    return render(
        request,
        "agg/books_all_detail.html",
        {
            "book_id": books_id[0],
            "book_name": books_name[0],
            "books_author": books_author[0],
            "books_price": books_price[0],
            "books_pages": books_pages[0],
            "books_rating": books_rating[0],
            "books_pubdate": books_pubdate[0],
            "books_publisher": books_publisher[0],
        }
    )


def author(request):
    authors_count = Author.objects.prefetch_related('authors').count()
    avg_author = Author.objects.all().aggregate(Avg('age'))
    min_author = Author.objects.all().aggregate(Min('age'))
    max_author = Author.objects.all().aggregate(Max('age'))

    return render(
        request,
        "agg/author.html",
        {'author': authors_count,
         'avg_author': int(avg_author['age__avg']),
         'min_author': min_author,
         'max_author': max_author,
         }
    )


def author_book_min(request, min_author):
    author_min = Author.objects.prefetch_related('book_set')
    authors_id = []
    authors_name = []
    authors_books = []
    authors_age = []
    for a in author_min:
        books = [book.name for book in a.book_set.all()]
        if a.age == min_author:
            authors_id.append(a.id)
            authors_name.append(a.name)
            authors_books.append(books)
            authors_age.append(a.age)

    return render(
        request,
        "agg/author_book_min.html",
        {
            "author_id": authors_id[0],
            "author_name": authors_name[0],
            "author_books": authors_books[0],
            "author_age": authors_age[0],

        }
    )


def author_book_max(request, max_author):
    author_max = Author.objects.prefetch_related('book_set')
    authors_id = []
    authors_name = []
    authors_books = []
    authors_age = []
    for a in author_max:
        books = [book.name for book in a.book_set.all()]
        if a.age == max_author:
            authors_id.append(a.id)
            authors_name.append(a.name)
            authors_books.append(books)
            authors_age.append(a.age)

    return render(
        request,
        "agg/author_book_max.html",
        {
            "author_id": authors_id[0],
            "author_name": authors_name[0],
            "author_books": authors_books[0],
            "author_age": authors_age[0],

        }
    )


def store(request):
    count_store = Store.objects.count()
    pop = Store.objects.annotate(number_of_books=Count('books__name'), average_price=Avg('books__price'))

    return render(
        request,
        "agg/store.html",
        {
            'pop': pop,
            'count_store': count_store
        }
    )


def store_books(request, store_id):
    queryset = Store.objects.prefetch_related('books')
    stores = []
    for store in queryset:
        books = [book for book in store.books.all()]
        if store.id == store_id:
            stores.append({
                'id': store.id, 'name': store.name, 'books': books,

            })

    return render(
        request,
        "agg/store_books.html",
        {
            'stores': stores,
        }
    )
