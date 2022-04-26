# Generated by Django 4.0.4 on 2022-04-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.TextField()),
            ],
        ),
    ]
