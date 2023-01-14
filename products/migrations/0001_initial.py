# Generated by Django 4.1.5 on 2023-01-12 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(upload_to='img', verbose_name='Фото')),
                ('weight', models.IntegerField(verbose_name='Вес')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('in_stock', models.IntegerField(default=0, verbose_name='В наличии')),
                ('sold', models.IntegerField(default=0, editable=False, verbose_name='Продано')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория')),
            ],
        ),
    ]