# Generated by Django 5.0.6 on 2024-09-13 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_alter_leave_remainingdays'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='remainingdays',
        ),
    ]
