# Generated by Django 4.2.3 on 2023-07-26 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventfinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
