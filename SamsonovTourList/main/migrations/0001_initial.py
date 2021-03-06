# Generated by Django 3.1.5 on 2021-01-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avilable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_id', models.IntegerField()),
                ('isAvilable', models.BinaryField()),
            ],
            options={
                'verbose_name': 'Возможно ли приехать',
                'verbose_name_plural': 'Возможно ли приехать',
            },
        ),
        migrations.CreateModel(
            name='ChillVariations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид путешествия',
                'verbose_name_plural': 'Вид путешествия',
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Имя гида')),
                ('rating', models.IntegerField(default='5', verbose_name='Рейтинг гида')),
            ],
            options={
                'verbose_name': 'Имя гида',
                'verbose_name_plural': 'Имя гида',
            },
        ),
        migrations.CreateModel(
            name='RatingPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_index', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Рейтинг места',
                'verbose_name_plural': 'Рейтинг места',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionName', models.CharField(max_length=40, verbose_name='Название региона')),
            ],
            options={
                'verbose_name': 'Название региона',
                'verbose_name_plural': 'Название региона',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('chilltype', models.IntegerField(default='0', verbose_name='Тип отдыха')),
                ('price', models.IntegerField(default='500', verbose_name='Цена (в руб)')),
            ],
            options={
                'verbose_name': 'Список туров',
                'verbose_name_plural': 'Список туров',
            },
        ),
        migrations.CreateModel(
            name='TaskDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateIn', models.DateField(verbose_name='DateIn')),
                ('dateOut', models.DateField(verbose_name='DateOut')),
            ],
            options={
                'verbose_name': 'Даты путешествия',
                'verbose_name_plural': 'Даты путешествия',
            },
        ),
        migrations.CreateModel(
            name='TaskTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeIn', models.TimeField(verbose_name='TimeIn')),
                ('timeOut', models.TimeField(verbose_name='TimeOut')),
            ],
            options={
                'verbose_name': 'Время путешествия',
                'verbose_name_plural': 'Время путешествия',
            },
        ),
    ]
