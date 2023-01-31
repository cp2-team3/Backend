# Generated by Django 4.1.5 on 2023-01-24 06:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hit', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('uploadImages', models.ImageField(blank=True, null=True, upload_to='')),
                ('uploadFiles', models.FileField(blank=True, null=True, upload_to='')),
                # ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='board.category')),
            ],
        ),
    ]
