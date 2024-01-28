# Generated by Django 5.0.1 on 2024-01-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='short_url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=20)),
                ('long_url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]