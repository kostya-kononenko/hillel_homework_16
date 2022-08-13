from django.contrib import admin

from.models import Author, Book, Publisher, Store


class BooksInline(admin.StackedInline):
    model = Book
    extra = 3


class StoresInline(admin.StackedInline):
    model = Store.books.through
    extra = 3


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Age information', {'fields': ['age'], 'classes': ['collapse']}),
    ]
    list_filter = ['age']
    search_fields = ['name']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    inlines = [BooksInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'rating', 'pubdate', 'publisher')
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['rating']}),
        (None, {'fields': ['pages']}),
        (None, {'fields': ['publisher']}),
        ('Price information', {'fields': ['price'], 'classes': ['collapse']}),
        ('Pubdate information', {'fields': ['pubdate'], 'classes': ['collapse']}),

    ]
    list_filter = ['pubdate']
    search_fields = ['name']
    date_hierarchy = 'pubdate'


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    inlines = [StoresInline]
