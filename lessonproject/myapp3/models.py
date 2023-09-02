from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    # def __str__(self):
    #     return f'Username: {self.name}, email: {self.email}, age:{self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # при удалении пользователя удаляются и все заказы
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    """ customer = models.ForeignKey(User, on_delete=models.CASCADE) 
    каждый заказ делает конкретный пользователь. У одного пользователя может
     быть несколько заказов, но заказ числится за одним пользователем
    ● products = models.ManyToManyField(Product) - заказ может содержать
    несколько разных продуктов. А продукт может входить в состав
    нескольких разных заказов """


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.content for post in posts)
        self.stdout.write(f'{intro}{text}')


"""
Здесь мы создаем метод "get_summary", который возвращает первые 12 слов
контента поста и добавляет многоточие в конце.
Вместо полного текста теперь можем получать первые несколько слов.
Django не ограничивает разработчика не методы внутри моделей. Подобный
подход, когда данные и расчёты производятся в моделях более
предпочтителен, чем расчёты внутри представлений по выгруженным из
модели данным. Тем более не стоит переносить расчёты в представления, о
которых мы будем подробно говорить на следующей лекции.
"""
