# Generated by Django 5.0.4 on 2024-04-18 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0006_remove_question_choices_choice_question_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_type',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
