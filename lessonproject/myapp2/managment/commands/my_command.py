from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Print 'Hello world!' to output."        
    #Создаём класс Command как дочерний для BaseCommand. 
    #Переменная help выведет справку по работе команды. 
    #А метод handle отработает при вызове команды в консоли.


    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!')   