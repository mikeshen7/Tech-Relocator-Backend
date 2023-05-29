# Generated by Django 4.2.1 on 2023-05-19 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('desired_location', models.CharField(max_length=64)),
                ('desired_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('experience', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('skills', models.CharField(max_length=64)),
                ('saved_locations', models.CharField(max_length=64)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]