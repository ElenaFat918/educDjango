Станислав Никуличев Создайте модель для запоминания бросков монеты: орёл или решка. Также запоминайте время броска.
Никита Шаверин from django.db import models
from datetime import datetime


class Kicks(models.Model):
result = models.BooleanField()
kick_time = models.DateTimeField(default=datetime.now())
Станислав Никуличев Доработаем задачу 1. Добавьте статический метод для статистики по n последним броскам монеты. Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
Никита Шаверин from django.db import models
from datetime import datetime
from random import randint


class Kicks(models.Model):
result = models.BooleanField()
kick_time = models.DateTimeField(default=datetime.now())

@staticmethod
def statistics(n: int):
reshka = 0
orel = 0
for _ in range(n):
kick = Kicks(result=randint(0, 1))
if kick.result:
reshka += 1
else:
orel += 1
result_dict = {
'орёл': orel,
'решка': reshka,
}
return result_dict
Станислав Никуличев Создайте модель Автор. Модель должна содержать следующие поля:
● имя до 100 символов
● фамилия до 100 символов
● почта
● биография
● день рождения
Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
Никита Шаверин class Author(models.Model):
name = models.CharField(max_length=100)
surname = models.CharField(max_length=100)
email = models.EmailField()
biography = models.TextField()
birthday = models.DateTimeField()

def __str__(self):
return f'{self.name} {self.surname}'
Белик Сергей python manage.py migrate
Белик Сергей запустим сервер?
Никита Шаверин from django.core.management.base import BaseCommand
from sem_2_1_app.models import Author
from datetime import datetime


class Command(BaseCommand):
help = 'Create authors'
def handle(self, *args, **kwargs):
for i in range(10):
author = Author(name=f'name_{i}', surname=f'surname_{i}', email=f'email_{i}@mail.ru',
biography='bla_bla_bla', birthday=datetime.now())
author.save()
self.stdout.write('authors created')
Станислав Никуличев Создайте модель Статья (публикация). Авторы из прошлой задачи могут писать статьи. У статьи может быть только один автор. У статьи должны быть следующие обязательные поля:
● заголовок статьи с максимальной длиной 200 символов
● содержание статьи
● дата публикации статьи
● автор статьи с удалением связанных объектов при удалении автора
● категория статьи с максимальной длиной 100 символов
● количество просмотров статьи со значением по умолчанию 0
● флаг, указывающий, опубликована ли статья со значением по умолчанию False
Белик Сергей так почему заполнил базу, но ругался на время????
Белик Сергей я вставил, все равно ошибка
Белик Сергей auto_now=True сработало, полет нормальный
Белик Сергей __str__?
Никита Шаверин class Article(models.Model):
head = models.CharField(max_length=200)
content = models.TextField()
public_date = models.DateTimeField(auto_now=True)
author = models.ForeignKey(Author, on_delete=models.CASCADE)
category = models.CharField(max_length=100)
count = models.IntegerField(default=0)
public = models.BooleanField()
Елена Фатхуллина author = Author.objects.filter(pk=pk).first()
Динис Абдурахманов Чё то не то
Белик Сергей базу отключи
Белик Сергей скинь код, плз
Белик Сергей без последнего скрипта все создалось, есть колонки
Никита Шаверин class Command(BaseCommand):
help = 'Create articles'
def handle(self, *args, **kwargs):
for author in Author.objects.all():
for i in range(randint(1, 5)):
article = Article(
head=f'head_{i}',
content=f'bla-bla-bla {i}',
author=author,
category=f'category_{i}',
public=randint(0,1),
)
article.save()
self.stdout.write('articles created')
Белик Сергей я просто вставлял твой код и все работает
Белик Сергей базу снеси и заново миграции и тд
Белик Сергей 4 команды
Белик Сергей удали конекты в базе и заново
Белик Сергей в дб
Белик Сергей from random import randint
from django.core.management import BaseCommand
from seminar_3_app.models import Author, Article


class Command(BaseCommand):
help = 'Create articles'

def handle(self, *args, **kwargs):
for author in Author.objects.all():
for i in range(randint(1, 5)):
article = Article(
head=f'head_{i}',
content=f'bla-bla-bla {i}',
author=author,
category=f'category_{i}',
public=randint(0, 1),
)
article.save()
self.stdout.write('articles created')
Белик Сергей class Article(models.Model):
head = models.CharField(max_length=200)
content = models.TextField()
public_date = models.DateTimeField(auto_now=True)
author = models.ForeignKey(Author, on_delete=models.CASCADE)
category = models.CharField(max_length=100)
count = models.IntegerField(default=0)
public = models.BooleanField()