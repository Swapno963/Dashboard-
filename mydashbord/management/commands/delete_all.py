# myapp/management/commands/delete_all_data.py

from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import connection

class Command(BaseCommand):
    help = 'Deletes all data from the database'

    def handle(self, *args, **kwargs):
        for model in apps.get_models():
            model.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all data'))

        # Optionally, reset auto-increment sequences if using PostgreSQL
        if connection.vendor == 'postgresql':
            with connection.cursor() as cursor:
                for table in connection.introspection.table_names():
                    cursor.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1")
            self.stdout.write(self.style.SUCCESS('Successfully reset auto-increment sequences'))
