# Generated by Django 2.2.4 on 2019-08-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
