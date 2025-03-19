from django.core.management.base import BaseCommand
import helpers


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('These are commands from commands.')
