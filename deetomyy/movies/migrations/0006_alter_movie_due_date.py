# Generated by Django 5.0.3 on 2024-04-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_order_movie_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
