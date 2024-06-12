# Generated by Django 5.0.4 on 2024-06-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0021_paymentdetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='user',
            name='expo_push_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_login',
            field=models.BooleanField(default=True),
        ),
    ]