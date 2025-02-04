# Generated by Django 5.1.3 on 2025-02-04 19:47

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_profile_delete_customuser'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', accounts.models.AccountManger()),
            ],
        ),
        migrations.RenameField(
            model_name='account',
            old_name='username',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
