# Generated by Django 3.1.5 on 2021-01-14 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210115_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='chilltype',
        ),
    ]
