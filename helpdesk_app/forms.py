from django.forms import ModelForm, ClearableFileInput, DateTimeInput
from helpdesk_app.models import Task


class CreateTaskForm(ModelForm):
    def save(self, commit=False):
        task = super(CreateTaskForm, self).save(commit=False)
        Task.objects.create(
            task_created_date=task.task_created_date,
            task_completed_date=task.task_completed_date,
            task_status=task.task_status,
            task_title=task.task_title,
            task_content=task.task_content,
            client_department=task.client_department,
            client_name=task.client_name,
            note=task.note,
            task_done_by=task.task_done_by
        )

    class Meta:
        model = Task
        fields = ['task_title', 'task_content', 'client_department', 'client_name']
        widgets = {
            'task_created_date': DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimefield'}),
            'task_completed_date': DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimefield'}),
        }
