# Generated by Django 4.0.5 on 2022-07-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_animal', models.CharField(max_length=30)),
                ('predador', models.CharField(max_length=3)),
                ('venenoso', models.CharField(max_length=3)),
                ('domestico', models.CharField(max_length=3)),
            ],
        ),
    ]
