# Generated by Django 5.1.3 on 2025-02-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_account_last_name_remove_account_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
