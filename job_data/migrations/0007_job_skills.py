# Generated by Django 4.2.1 on 2023-05-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_data', '0006_alter_job_education_alter_job_employment_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
