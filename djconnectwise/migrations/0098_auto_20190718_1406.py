# Generated by Django 2.1 on 2019-07-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0097_merge_20190718_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='agreement_id',
        ),
        migrations.AddField(
            model_name='ticket',
            name='agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agreement_tickets', to='djconnectwise.Agreement'),
        ),
    ]
