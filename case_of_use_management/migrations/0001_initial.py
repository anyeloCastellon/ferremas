# Generated by Django 3.1.3 on 2023-10-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('incident_handler_management', '0001_initial'),
        ('user_management', '0005_company_abbreviation'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignatureCiber',
            fields=[
                ('enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id_signature_ciber', models.AutoField(primary_key=True, serialize=False)),
                ('name_signature_ciber', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'SignatureCiber',
                'verbose_name_plural': 'SignatureCiber',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='TypeRule',
            fields=[
                ('enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id_type_rule', models.AutoField(primary_key=True, serialize=False)),
                ('name_type_rule', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'TypeRule',
                'verbose_name_plural': 'TypeRule',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='TypeTech',
            fields=[
                ('enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id_type_tech', models.AutoField(primary_key=True, serialize=False)),
                ('name_type_tech', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'TypeTech',
                'verbose_name_plural': 'TypeTech',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='CaseUse',
            fields=[
                ('enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id_case_of_use', models.AutoField(primary_key=True, serialize=False)),
                ('name_case_of_use', models.CharField(max_length=1256)),
                ('company', models.ManyToManyField(blank=True, to='user_management.Company')),
                ('incident', models.ManyToManyField(blank=True, to='incident_handler_management.Incident')),
                ('siem', models.ManyToManyField(blank=True, to='user_management.SIEM')),
                ('signature_ciber', models.ManyToManyField(blank=True, to='case_of_use_management.SignatureCiber')),
                ('type_incident', models.ManyToManyField(blank=True, to='incident_handler_management.TypeIncident')),
                ('type_rule', models.ManyToManyField(blank=True, to='case_of_use_management.TypeRule')),
                ('type_tech', models.ManyToManyField(blank=True, to='case_of_use_management.TypeTech')),
            ],
            options={
                'verbose_name': 'CaseUse',
                'verbose_name_plural': 'CaseUse',
                'ordering': ('-created_date',),
            },
        ),
    ]