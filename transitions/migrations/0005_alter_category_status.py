# Generated by Django 5.1.3 on 2025-01-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transitions', '0004_rename_statuse_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('expose', 'income')], default='expose', max_length=200, null=True),
        ),
    ]
