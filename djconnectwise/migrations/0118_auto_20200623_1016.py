# Generated by Django 2.1.14 on 2020-06-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0117_auto_20200609_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='office_email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
    ]
