# Generated by Django 5.0.4 on 2024-06-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0028_remove_survey_user_survey_user_create_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='survey_user_done',
            field=models.ManyToManyField(related_name='survey_user_done', to='apartments.survey'),
        ),
    ]
