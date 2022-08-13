from agg.models import Publisher
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker(['it_IT', 'en_US'])


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=1, type=int, help='Indicates the number of Publisher to be created')

    def handle(self, *args, **numbers):
        publishers = []
        for i in range(numbers["total"][0]):
            publishers.append(Publisher(name=fake.name()))
        Publisher.objects.bulk_create(publishers)
