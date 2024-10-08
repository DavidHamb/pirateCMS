# Generated by Django 5.0.7 on 2024-07-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_case_os_case_address_case_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('port', models.CharField(blank=True, max_length=10, null=True)),
                ('version', models.CharField(blank=True, max_length=10, null=True)),
                ('checked', models.BooleanField(default=False)),
                ('vulnerable', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
