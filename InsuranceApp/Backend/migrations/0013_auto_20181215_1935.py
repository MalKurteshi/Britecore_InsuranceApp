# Generated by Django 2.1.2 on 2018-12-15 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0012_auto_20181215_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regpolicies',
            name='RegPolicies_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
