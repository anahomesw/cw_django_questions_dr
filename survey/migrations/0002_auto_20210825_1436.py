# Generated by Django 3.1.2 on 2021-08-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='dislike',
            field=models.PositiveIntegerField(default=0, verbose_name='Disike'),
        ),
        migrations.AddField(
            model_name='answer',
            name='like',
            field=models.PositiveIntegerField(default=0, verbose_name='Like'),
        ),
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.PositiveIntegerField(default=0, verbose_name='Puntos'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='value',
            field=models.PositiveIntegerField(default=10, verbose_name='Respuesta'),
        ),
    ]
