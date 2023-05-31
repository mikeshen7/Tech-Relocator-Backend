# Generated by Django 4.2.1 on 2023-05-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.DecimalField(decimal_places=1, max_digits=5)),
                ('city', models.CharField(max_length=64)),
                ('state_code', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=64)),
            ],
        ),
    ]
