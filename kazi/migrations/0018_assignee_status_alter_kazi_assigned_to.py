# Generated by Django 4.1.3 on 2022-11-26 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kazi', '0017_alter_assignee_kazi'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignee',
            name='status',
            field=models.CharField(blank=True, default='WAITING', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='kazi',
            name='assigned_to',
            field=models.CharField(default=None, max_length=50, verbose_name='Assignee'),
        ),
    ]
