from django.core.management.base import BaseCommand

from api.factory import ClientFactory


class Command(BaseCommand):
    help = 'Fill the database Client with random value.'

    def add_arguments(self, parser):
        parser.add_argument('--nbr_client',
                            default=3,
                            type=int,
                            help='The number of fake client to create.')

    def handle(self, *args, **options):
        for _ in range(options['nbr_client']):
            ClientFactory()
