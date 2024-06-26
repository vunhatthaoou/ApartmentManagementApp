# Generated by Django 5.0.4 on 2024-04-18 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_receipt_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('content', models.CharField(max_length=255)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.survey')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]
