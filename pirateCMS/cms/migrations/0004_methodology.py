# Generated by Django 5.0.7 on 2024-07-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Methodology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('cve', models.CharField(blank=True, max_length=20, null=True)),
                ('service', models.CharField(blank=True, max_length=250, null=True)),
                ('version', models.CharField(blank=True, max_length=10, null=True)),
                ('documents', models.CharField(blank=True, max_length=100, null=True)),
                ('urls', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
