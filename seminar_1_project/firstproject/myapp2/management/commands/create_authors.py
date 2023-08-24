from django.core.management import BaseCommand
from myapp2.models import Author
from datetime import datetime


class Command(BaseCommand):
    help = 'Create authors'

    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(name=f'name_{i}',
                            surname=f'surname_{i}',
                            email=f'email_{i}@mail.ru',
                            biography='bla_bla_bla',
                            birthday=datetime.now())
            author.save()
            self.stdout.write('authors created')

 #    python manage.py create_authors