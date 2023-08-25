from django.core.management.base import BaseCommand
from myapp2.models import User
"""
QuerySet объект множества создает связь между БД и моделью и хранит записи что мы извлекли из БД.
"""
class Command(BaseCommand):
    help = "Get user by id."

        def add_arguments(self, parser):    # Метод add_arguments позволяет парсить командную строку,  обработчик handler может получить к идентификатору доступ через ключ словаря kwargs.
            parser.add_argument('id', type=int, help='User ID')

        def handle(self, *args, **kwargs):
            id = kwargs['id']
            user = User.objects.get(id=id)  
            self.stdout.write(f'{user}')

from django.core.management.base import BaseCommand
from myapp2.models import User

# class Command(BaseCommand):
# help = "Get user by id."

#     def add_arguments(self, parser):
#         parser.add_argument('pk', type=int, help='User ID')

#     def handle(self, *args, **kwargs):
#         pk = kwargs['pk']
#         user = User.objects.filter(pk=pk).first() 
#         self.stdout.write(f'{user}')