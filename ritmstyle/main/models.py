from django.db import models
from django.urls import reverse


class News(models.Model):
    news_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    news_title = models.CharField(max_length=255, verbose_name="Заголовок новости")
    news_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    news_text = models.TextField(blank=True, verbose_name="Текст новости")
    news_img = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Картинка новости")
    news_date = models.DateField(auto_now_add=True, verbose_name="Дата новости")

    def __str__(self):
        return self.news_title

    def get_absolute_url(self):
        return reverse('show_news', kwargs={'news_slug': self.news_slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['news_date', 'news_title']


class Blog(models.Model):
    blog_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    blog_title = models.CharField(max_length=255, verbose_name='Заголовок блога')
    blog_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    blog_text = models.TextField(blank=True, verbose_name='Текст блога')
    blog_img = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Картинка блога')
    blog_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse('show_blog_post', kwargs={'blog_slug': self.blog_slug})

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Посты блога"
        ordering = ['blog_date', 'blog_title']


class Reviews(models.Model):
    reviews_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    reviews_client = models.CharField(max_length=255, verbose_name='Клиент')
    reviews_text = models.TextField(max_length=550, verbose_name='Отзыв')

    def __str__(self):
        return self.reviews_client

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['reviews_client', 'reviews_text']


class Services(models.Model):
    services_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    services_name = models.CharField(max_length=255, verbose_name='Название услуги')
    services_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена услуги')
    services_description = models.TextField(max_length=700, verbose_name='Описание услуги')

    def __str__(self):
        return self.services_name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['services_name', 'services_price']


class Addresses(models.Model):
    addresses_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    addresses_name = models.CharField(max_length=150, verbose_name='Адрес')

    def __str__(self):
        return self.addresses_name

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['addresses_id', 'addresses_name']


class Visit(models.Model):
    visit_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    visit_first_name = models.CharField(max_length=150, verbose_name='Имя')
    visit_last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    visit_patronymic = models.CharField(max_length=150, verbose_name='Отчество')
    visit_email = models.EmailField(verbose_name='Почта')
    visit_phone = models.CharField(max_length=12, verbose_name='Норме телефона')
    visit_time = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время посещения')
    visit_is_happened = models.BooleanField(default=False)
    services = models.ForeignKey('Services', on_delete=models.CASCADE)
    addresses = models.ForeignKey('Addresses', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['visit_first_name', 'visit_last_name', 'visit_patronymic']
