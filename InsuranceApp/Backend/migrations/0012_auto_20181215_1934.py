# Generated by Django 2.1.2 on 2018-12-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0011_regpolicies_regpolicies_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regpolicies',
            name='RegPolicies_username',
            field=models.ForeignKey(db_column='RegUser_username', on_delete='CASCADE', to='Backend.RegUser'),
        ),
    ]