from aggnew.models import Store

from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker(['it_IT', 'en_US'])


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=1, type=int, help='Indicates the number of Stores to be created')

    def handle(self, *args, **numbers):
        stores = []
        for i in range(numbers["total"][0]):
            stores.append(Store(name=fake.sentence()))
        Store.objects.bulk_create(stores)
