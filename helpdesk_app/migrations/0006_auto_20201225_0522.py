# Generated by Django 2.2.15 on 2020-12-25 05:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk_app', '0005_task_task_done_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Müraciət tarixi'),
        ),
    ]
