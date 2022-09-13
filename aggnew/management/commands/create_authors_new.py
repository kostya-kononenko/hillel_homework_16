import random

from aggnew.models import Author

from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker(['it_IT', 'en_US'])


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=1, type=int, help='Indicates the number of Authors to be created')

    def handle(self, *args, **numbers):
        authors = []
        for i in range(numbers["total"][0]):
            authors.append(Author(
                name=fake.name(),
                age=random.randint(18, 100)
            ))
        Author.objects.bulk_create(authors)
