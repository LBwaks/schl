# Generated by Django 4.1.3 on 2022-11-25 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kazi', '0014_alter_assignee_assignee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignee',
            name='assigner',
        ),
    ]
