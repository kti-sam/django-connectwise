# Generated by Django 3.1 on 2020-09-23 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0124_auto_20200917_1922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agreement',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='projectteammember',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='workrole',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='worktype',
            options={'get_latest_by': 'modified'},
        ),
    ]
