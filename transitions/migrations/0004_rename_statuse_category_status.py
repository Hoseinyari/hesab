# Generated by Django 5.1.3 on 2025-01-24 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transitions', '0003_alter_category_statuse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='statuse',
            new_name='status',
        ),
    ]
