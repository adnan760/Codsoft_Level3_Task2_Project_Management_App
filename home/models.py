from django.db import models

class Task(models.Model):
    Priority =(('Low','Low'),
                ('Medium','Medium'),
                ('High','High'))
    project_name = models.CharField(max_length=200)
    task_name = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=300,default=None, null = True, blank=True)
    due_date = models.DateTimeField(default=None, null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=8, choices=Priority, default='L')

    def __str__(self):
        return self.task_name