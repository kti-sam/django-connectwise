# Generated by Django 2.0 on 2018-12-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0080_auto_20181210_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.CharField(blank=True, help_text='Member Avatar', max_length=300, null=True, verbose_name='Member Avatar'),
        ),
    ]
