# Generated by Django 5.0.4 on 2024-05-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0019_alter_receipt_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='order_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]