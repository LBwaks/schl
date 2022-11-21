# Generated by Django 4.1.3 on 2022-11-18 08:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Course Name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('description', models.TextField(verbose_name='About Course')),
                ('is_published', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_course', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kazi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kazi_id', models.CharField(max_length=50, verbose_name='kazi_id')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('unit', models.CharField(max_length=50, verbose_name='Unit Name')),
                ('description', ckeditor.fields.RichTextField()),
                ('due', models.DateTimeField(verbose_name='Time Due')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kazi.course', verbose_name='Course')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_kazi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Work Type ')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('description', models.TextField(verbose_name='About Work Type ')),
                ('is_published', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_workType', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KaziImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='kazi/', verbose_name='')),
                ('updated_date', models.DateField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('kazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kazi.kazi', verbose_name='Kazi Image')),
            ],
        ),
        migrations.AddField(
            model_name='kazi',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kazi.worktype', verbose_name='Work Type'),
        ),
    ]