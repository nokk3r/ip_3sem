# Generated by Django 3.1.5 on 2021-01-14 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210115_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цена',
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=20, verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Приоритет',
                'verbose_name_plural': 'Приоритет',
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='price',
        ),
        migrations.AddField(
            model_name='guide',
            name='Region_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.region', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='avilable',
            name='Priority_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.priority', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='task',
            name='Pricing_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.pricing', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='task',
            name='Priority_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.priority', verbose_name='Регион'),
        ),
    ]
