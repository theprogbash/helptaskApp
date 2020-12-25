from django.contrib import admin
from helpdesk_app.models import *
admin.site.site_header = "Azərsığorta | Helpdesk Admin Panel"
admin.site.site_title = "Azərsığorta | Helpdesk"

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['task_created_date', 'task_content', 'client_department', 'client_name']

admin.site.register(Reason)
admin.site.register(Department)
admin.site.register(Task, TaskAdmin)