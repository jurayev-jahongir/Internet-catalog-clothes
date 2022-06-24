from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Ключ')
    img = models.ImageField(upload_to='img/', verbose_name='Фото для категория')
    text = models.TextField(verbose_name='Описание')
    date = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создание')
    date_update = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар')
    price = models.IntegerField(verbose_name='Цена')
    img = models.ImageField(upload_to='img/', verbose_name='Фото Товара')
    text = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    date = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Network(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    network = models.CharField(max_length=200, verbose_name='Ссылка')
    date = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='')
    date_update = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='')

    class Meta:
        verbose_name = 'Соц сеть'
        verbose_name_plural = 'Соц сети'

    def __str__(self):
        return self.name


class Main(models.Model):
    name = models.CharField(max_length=200, verbose_name='Город')
    text = models.TextField( verbose_name='Текст')
    date = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='')
    date_update = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='')

    class Meta:
        verbose_name = 'Главный информация'
        verbose_name_plural = 'Главные информации'

    def __str__(self):
        return self.name


class Our(models.Model):
    name = models.TextField(verbose_name='О магазине')
    text = models.CharField(max_length=200, verbose_name='Адрес')
    date = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='')
    date_update = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='')

    class Meta:
        verbose_name = 'О нас имформация '
        verbose_name_plural = 'О нас информации'

    def __str__(self):
        return self.name

