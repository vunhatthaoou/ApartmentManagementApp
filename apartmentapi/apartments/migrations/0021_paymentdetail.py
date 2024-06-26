# Generated by Django 5.0.4 on 2024-05-29 16:30

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0020_receipt_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('receipt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apartments.receipt')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]
