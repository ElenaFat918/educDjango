Ващенко Антон
from django.core.management.base import BaseCommand
from seminar2_app2.models import Author, Post, Comment
from random import randint, choice


class Command(BaseCommand):
    help = 'Fill db by fake data'

    def handle(self, *args, **options):
        for i in range(5):
            author = Author(name=f'Name{i + 1}', surname=f'Surname{i + 1}', email=f'name_surname{i + 1}@gmail.com',
                            birthdate=f'{randint(1700, 1950)}-{randint(1, 12)}-{randint(1, 28)}',
                            biography='Some biography')
            author.save()
            for j in range(1, 4):
                post = Post(title=f'Title{i * 3 + j}', content='Some content', category='SomeCategory', author=author)
                post.save()

        authors = [*Author.objects.all()]
        for post in Post.objects.all():
            for i in range(3):
                comment = Comment(author=choice(authors), post=post, comment='Some comment')
                comment.save()

20:13
Станислав Никуличев
Доработаем задачу 4. Создай шаблон для вывода подробной информации о статье. Внесите изменения в views.py - создайте представление и в urls.py - добавьте маршрут.