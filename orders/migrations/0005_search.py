# Generated by Django 3.1.12 on 2022-04-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_delete_marker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
