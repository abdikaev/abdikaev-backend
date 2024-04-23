from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movie_items_movie_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='order',
            new_name='owner',
        ),
    ]
