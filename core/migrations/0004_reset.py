# Generated by Django 4.1.5 on 2023-01-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_usertoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('token', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
