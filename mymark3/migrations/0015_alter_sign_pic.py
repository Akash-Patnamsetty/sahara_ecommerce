# Generated by Django 5.1.7 on 2025-05-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymark3', '0014_alter_log_in_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/static/images'),
        ),
    ]
