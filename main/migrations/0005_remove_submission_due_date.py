# Generated by Django 5.1.5 on 2025-02-10 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_assignment_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='due_date',
        ),
    ]
