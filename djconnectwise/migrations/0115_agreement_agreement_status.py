# Generated by Django 2.1.11 on 2020-04-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0114_auto_20200219_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='agreement_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
