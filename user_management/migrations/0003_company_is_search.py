# Generated by Django 3.1.3 on 2023-01-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_company_domain_id_qradar'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_search',
            field=models.BooleanField(default=True),
        ),
    ]