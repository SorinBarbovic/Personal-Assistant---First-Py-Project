# Generated by Django 4.1 on 2022-10-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_delete_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='holiday_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
