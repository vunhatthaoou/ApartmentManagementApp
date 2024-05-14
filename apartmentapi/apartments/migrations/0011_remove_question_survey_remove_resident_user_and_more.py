# Generated by Django 5.0.4 on 2024-05-14 12:28

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0010_remove_choice_question_choice_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='resident',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='ecabinet',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='flat',
            name='description',
        ),
        migrations.AddField(
            model_name='ecabinet',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ecabinet',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ecabinet',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='total',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='carcard',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='tag',
        ),
        migrations.AlterField(
            model_name='flat',
            name='e_cabinet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='apartments.ecabinet'),
        ),
        migrations.AlterField(
            model_name='like',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='survey',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Resident',
        ),
        migrations.AddField(
            model_name='complaint',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='apartments.tag'),
        ),
    ]
