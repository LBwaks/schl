# Generated by Django 4.1.3 on 2022-11-23 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kazi', '0007_educationlevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='kazi',
            name='level',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='kazi.educationlevel', verbose_name='Education Level'),
            preserve_default=False,
        ),
    ]
