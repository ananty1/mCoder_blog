# Generated by Django 4.2.3 on 2023-07-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=40)),
                ('content', models.TextField()),
            ],
        ),
    ]
