# Generated by Django 4.1 on 2022-08-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.PositiveBigIntegerField()),
                ('task_name', models.CharField(max_length=60)),
                ('task_description', models.CharField(max_length=180)),
                ('task_category', models.CharField(max_length=60)),
                ('task_status', models.CharField(max_length=60)),
                ('task_created_date', models.DateTimeField()),
                ('task_due_date', models.DateTimeField()),
                ('task_completed_date', models.DateTimeField()),
            ],
        ),
    ]
