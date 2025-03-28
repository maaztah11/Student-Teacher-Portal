# Generated by Django 5.1.5 on 2025-01-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('room', models.ManyToManyField(related_name='room', to='main.classroom')),
                ('sent_by', models.ManyToManyField(related_name='sender', to='main.teacher')),
            ],
        ),
    ]
