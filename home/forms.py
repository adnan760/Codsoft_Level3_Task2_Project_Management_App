from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project_name','task_name', 'assigned_to', 'priority','due_date']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project_name','task_name', 'assigned_to', 'due_date', 'priority', 'completed']