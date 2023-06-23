# Generated by Django 4.2.2 on 2023-06-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True, max_length=500)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
