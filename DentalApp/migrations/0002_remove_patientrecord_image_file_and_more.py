# Generated by Django 5.1.7 on 2025-03-22 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DentalApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientrecord',
            name='image_file',
        ),
        migrations.RemoveField(
            model_name='patientrecord',
            name='upload_date',
        ),
    ]
