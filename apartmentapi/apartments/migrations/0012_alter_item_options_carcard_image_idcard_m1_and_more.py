# Generated by Django 5.0.4 on 2024-05-14 16:52

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0011_remove_question_survey_remove_resident_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='carcard',
            name='image_idcard_m1',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carcard',
            name='image_idcard_m2',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carcard',
            name='image_mrc_m1',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carcard',
            name='image_mrc_m2',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]