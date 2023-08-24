from random import randint

from django.core.management import BaseCommand
from myapp2.models import Author, Article


class Command(BaseCommand):
    help = 'Create articles'

    def handle(self, *args, **kwargs):
        for author in Author.objects.all():
            for i in range(randint(1, 5)):
                article = Article(head=f'head_{i}',
                                  content=f'bla-bla-bla {i}',
                                  author=author,
                                  category=f'category_{i}',
                                  public=randint(0,1),)
                article.save()
                self.stdout.write('articles created')

#   python manage.py  create_articles