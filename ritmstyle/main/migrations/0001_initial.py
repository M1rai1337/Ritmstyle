# Generated by Django 4.1.7 on 2023-04-18 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('addresses_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresses_name', models.CharField(max_length=150, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
                'ordering': ['addresses_id', 'addresses_name'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255, verbose_name='Заголовок блога')),
                ('blog_slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('blog_text', models.TextField(blank=True, verbose_name='Текст блога')),
                ('blog_img', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка блога')),
                ('blog_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Посты блога',
                'ordering': ['blog_date', 'blog_title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=255, verbose_name='Заголовок новости')),
                ('news_slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('news_text', models.TextField(blank=True, verbose_name='Текст новости')),
                ('news_img', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка новости')),
                ('news_date', models.DateField(auto_now_add=True, verbose_name='Дата новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['news_date', 'news_title'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('reviews_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews_client', models.CharField(max_length=255, verbose_name='Клиент')),
                ('reviews_text', models.TextField(max_length=550, verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['reviews_client', 'reviews_text'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('services_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_name', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('services_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена услуги')),
                ('services_description', models.TextField(max_length=700, verbose_name='Описание услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['services_name', 'services_price'],
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('visit_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('visit_last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('visit_patronymic', models.CharField(max_length=150, verbose_name='Отчество')),
                ('visit_email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('visit_phone', models.CharField(max_length=12, verbose_name='Норме телефона')),
                ('visit_time', models.DateTimeField(verbose_name='Дата и время посещения')),
                ('visit_is_happened', models.BooleanField(default=False)),
                ('addresses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.addresses')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.services')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ['visit_first_name', 'visit_last_name', 'visit_patronymic'],
            },
        ),
    ]
