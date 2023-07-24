# Generated by Django 4.2.3 on 2023-07-24 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventfinder', '0002_rename_eventfavorites_eventfavorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='tickerPrice',
            new_name='ticket',
        ),
        migrations.AlterField(
            model_name='event',
            name='categoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_set', to='eventfinder.eventcategory'),
        ),
        migrations.AlterField(
            model_name='eventcategory',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]