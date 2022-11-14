# Generated by Django 3.2 on 2022-11-14 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('position', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('work_experience', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VIPClient',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.client')),
                ('vip_status_start', models.DateField()),
                ('donation_amount', models.IntegerField()),
                ('vip_client', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('employee.client',),
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.IntegerField()),
                ('id_card', models.CharField(max_length=20)),
                ('person_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('work_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.workproject')),
            ],
        ),
    ]
