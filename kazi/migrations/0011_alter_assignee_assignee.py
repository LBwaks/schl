# Generated by Django 4.1.3 on 2022-11-25 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kazi', '0010_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignee',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_kazi_assignee', to=settings.AUTH_USER_MODEL),
        ),
    ]
