# Generated by Django 5.0.7 on 2024-07-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_book_created_remove_book_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(),
        ),
    ]
