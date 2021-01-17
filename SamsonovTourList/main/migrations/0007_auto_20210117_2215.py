# Generated by Django 3.1.5 on 2021-01-17 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210115_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='TaskDate_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.taskdate', verbose_name='Дата поездки'),
        ),
        migrations.AddField(
            model_name='ratingplace',
            name='Region_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.region', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='taskdate',
            name='TaskTime_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tasktime', verbose_name='Время поездки'),
        ),
    ]