# Generated by Django 4.1.2 on 2022-10-06 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleListApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.BigIntegerField(unique=True),
        ),
    ]
