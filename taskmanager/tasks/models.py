from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    task_number = models.PositiveBigIntegerField()
    task_name = models.CharField (max_length=60)
    task_description = models.CharField (max_length=180)
    task_category = models.CharField (max_length=60)
    task_status = models.CharField (max_length=60)
    task_created_date = models.DateTimeField (default=datetime.now)
    task_due_date = models.DateTimeField (null=True)
    task_completed_date = models.DateTimeField (null=True)
    task_comment = models.CharField (max_length=180, null=True)
    #task_complete = models.BooleanField(default=False)
    # task_duration = models.DurationField()

    def __str__(self):
        return f'Task: {self.task_name}'

    # class Meta:
    #     ordering = ['task_complete']

class Holiday(models.Model):
    holiday_number = models.PositiveBigIntegerField()
    holiday_type = models.CharField (max_length=60)
    holiday_description = models.CharField (max_length=180)
    holiday_from = models.CharField (max_length=60)
    holiday_to = models.CharField (max_length=60)
    holiday_status = models.CharField (max_length=60)
    holiday_start_date = models.DateTimeField (default=datetime.now)
    holiday_end_date = models.DateTimeField (null=True)
    holiday_budget = models.PositiveBigIntegerField()
    holiday_comment = models.CharField (max_length=180, null=True)

    def __str__(self):
        return f'Holiday: {self.holiday_number}'

class Shopping(models.Model):
    shopping_list_number = models.PositiveBigIntegerField()
    shopping_description = models.CharField (max_length=180)
    shopping_market = models.CharField (max_length=60)
    shopping_quantity = models.PositiveBigIntegerField()
    shopping_status = models.CharField (max_length=60)
    shopping_budget = models.PositiveBigIntegerField()
    shopping_deadline = models.DateTimeField (default=datetime.now)
    shopping_comment = models.CharField (max_length=180, null=True)

    def __str__(self):
        return f'Shopping: {self.shopping_list_number}'

# class complete (models.Model):
#     mark_complete = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.text