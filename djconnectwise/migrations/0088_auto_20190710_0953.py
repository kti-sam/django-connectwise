# Generated by Django 2.1 on 2019-07-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0087_auto_20190705_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeentry',
            name='billable_option',
            field=models.CharField(choices=[('Billable', 'Billable'), ('DoNotBill', 'Do Not Bill'), ('NoCharge', 'No Charge')], max_length=250),
        ),
    ]
