# Generated by Django 3.1.2 on 2021-08-25 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20210825_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='points',
            new_name='ranking',
        ),
    ]