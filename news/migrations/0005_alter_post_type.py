# Generated by Django 4.2.9 on 2024-01-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_text_of_comm_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('A', 'A'), ('N', 'N')], default='N', max_length=1),
        ),
    ]
