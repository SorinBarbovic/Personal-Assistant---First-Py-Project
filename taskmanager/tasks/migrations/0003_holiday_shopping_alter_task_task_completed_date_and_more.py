# Generated by Django 4.1 on 2022-09-24 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_task_comment_alter_task_task_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_number', models.PositiveBigIntegerField()),
                ('holiday_type', models.CharField(max_length=60)),
                ('holiday_description', models.CharField(max_length=180)),
                ('holiday_from', models.CharField(max_length=60)),
                ('holiday_to', models.CharField(max_length=60)),
                ('holiday_status', models.CharField(max_length=60)),
                ('holiday_start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('holiday_end_date', models.DateTimeField(default=datetime.datetime.now)),
                ('holiday_budget', models.PositiveBigIntegerField()),
                ('holiday_comment', models.CharField(max_length=180, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_list_number', models.PositiveBigIntegerField()),
                ('shopping_description', models.CharField(max_length=180)),
                ('shopping_market', models.CharField(max_length=60)),
                ('shopping_quantity', models.PositiveBigIntegerField()),
                ('shopping_status', models.CharField(max_length=60)),
                ('shopping_budget', models.PositiveBigIntegerField()),
                ('shopping_deadline', models.DateTimeField(default=datetime.datetime.now)),
                ('shopping_comment', models.CharField(max_length=180, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='task_completed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]