# Generated by Django 4.2.3 on 2023-08-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventfinder', '0002_alter_event_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='inFav',
            field=models.BooleanField(default=False),
        ),
    ]
