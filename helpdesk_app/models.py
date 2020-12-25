from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    name = models.CharField(_('Departamentin adı'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Departament'
        verbose_name_plural = 'Departamentlər'

class Reason(models.Model):
    name = models.CharField(_('Müraciət səbəbi'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Müraciət səbəbi'
        verbose_name_plural = 'Müraciət səbəbləri'

class Task(models.Model):
    TASK_STATUS = (
        ("İmtina edilib", "İmtina edilib"),
        ("Gözləmədədir", "Gözləmədədir"),
        ("İcra edilib", "İcra edilib")
    )
    task_created_date = models.DateTimeField(_('Müraciət tarixi'), default=timezone.now, blank=True, null=True)
    task_completed_date = models.DateTimeField(_('Müraciətin icra tarixi'), blank=True, null=True)
    task_status = models.CharField(_('Müraciətin statusu'), choices = TASK_STATUS, max_length=30, default="Gözləmədədir")
    task_title = models.ForeignKey('Reason', on_delete = models.CASCADE)
    task_content = models.TextField(_('Müraciətin məzmunu'), blank=True, null=True, max_length = 200)
    client_department = models.ForeignKey('Department', on_delete = models.CASCADE)
    client_name = models.CharField(_('Müraciət edən işçi'), blank=True, null=True, max_length = 60)
    note = models.TextField(_('Müraciətin icrası haqqında məlumat'), blank=True, null=True, max_length = 200)
    task_done_by = models.ForeignKey('account_app.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.task_created_date)

    class Meta:
        verbose_name = 'Tapşırıq'
        verbose_name_plural = 'Tapşırıqlar'