from django.core.management.base import BaseCommand, CommandError
import user_activity.setup as setup


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        setup.setup_user_groups(self.stdout)
