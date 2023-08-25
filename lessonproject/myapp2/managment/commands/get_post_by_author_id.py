from django.core.management.base import BaseCommand
from myapp2.models import Author, Post

class Command(BaseCommand):
    help = "Get all posts by author id."
    
    def add_arguments(self, parser):    # добавляем pk для извлечения id автора
        parser.add_argument('pk', type=int, help='User ID')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')   # извлекаем pk из командной строки чтобы получить целое число - User ID автора
        author = Author.objects.filter(pk=pk).first()   # находим одного конкретного автора, чей id=переданному значению
        if author is not None:  # если такой автор не None, то извлекаем посты
            posts = Post.objects.filter(author=author)  # находим посты, которые написал этот автор (без фильтра)
            intro = f'All posts of {author.name}\n' # определяем строку "все посты конкретного автора"
            text = '\n'.join(post.content for post in posts)    # собираем все посты этого автора воедино в переменную text
            self.stdout.write(f'{intro}{text}')
"""
# В переменной posts будет объект QuerySet со всеми постами написанными этим автором. 
# Мы можем работать с объектом QuerySet как с питоновскими списками и коллекциями, 
т.е. for post in posts мы начинаем перебирать все посты и для каждого поста мы извлекаем параметр content - 
cодержимое поста и формируем некую строку с содержимым всех постов.

"""

#  если нам не нужно имя автора в строке intro фильтруем посты по автору непосредственно из модели пост:

    # def handle(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     posts = Post.objects.filter(author__pk=pk)
    #     intro = f'All posts\n'
    #     text = '\n'.join(post.content for post in posts)
    #     self.stdout.write(f'{intro}{text}')