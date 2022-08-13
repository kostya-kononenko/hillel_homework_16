import random

from agg.models import Book

from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker(['it_IT', 'en_US'])


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=1, type=int, help='Indicates the number of Books to be created')

    def handle(self, *args, **numbers):
        books = []
        for i in range(numbers["total"][0]):
            books.append(Book(
                name=fake.sentence(),
                pages=random.randint(50, 1000),
                price=random.randint(5, 500),
                rating=random.randint(1, 10),
                pubdate=fake.date(),
                publisher_id=random.randint(1, 40)
            ))
        Book.objects.bulk_create(books)
