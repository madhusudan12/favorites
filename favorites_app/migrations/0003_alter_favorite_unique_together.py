# Generated by Django 4.2.3 on 2023-07-23 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites_app', '0002_alter_favorite_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set(),
        ),
    ]
