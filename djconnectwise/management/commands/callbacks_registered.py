from django.core.management.base import BaseCommand, CommandError
from djconnectwise.callbacks import CallbacksHandler
from djconnectwise.api import ConnectWiseAPIError


class Command(BaseCommand):
    help = 'Ensure callbacks are registered on ConnectWise.'

    def handle(self, *args, **options):
        handler = CallbacksHandler()
        try:
            handler.ensure_registered()
        except ConnectWiseAPIError as e:
            raise CommandError(e)
