# Generated by Django 2.1.3 on 2018-11-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0005_auto_20181111_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reguser',
            old_name='RegUser_address',
            new_name='RegUser_city',
        ),
        migrations.RemoveField(
            model_name='reguser',
            name='id',
        ),
        migrations.AddField(
            model_name='reguser',
            name='RegUser_contry',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguser',
            name='RegUser_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguser',
            name='RegUser_streetaddress',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguser',
            name='RegUser_zipcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reguser',
            name='RegUser_birthday',
            field=models.DateField(),
        ),
    ]
