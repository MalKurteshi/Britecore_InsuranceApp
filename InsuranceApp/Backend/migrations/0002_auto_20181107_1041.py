# Generated by Django 2.1.2 on 2018-11-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RegUser_name', models.CharField(max_length=50)),
                ('RegUser_surname', models.CharField(max_length=50)),
                ('RegUser_email', models.CharField(max_length=20)),
                ('RegUser_username', models.CharField(max_length=15)),
                ('RegUser_birthday', models.DateTimeField()),
                ('RegUser_photo', models.URLField()),
                ('RegUsers_address', models.CharField(max_length=50)),
                ('RegUsers_password', models.CharField(max_length=15)),
                ('RegUsers_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
