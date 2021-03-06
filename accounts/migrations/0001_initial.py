# Generated by Django 3.0.3 on 2020-05-07 01:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_allocated', models.IntegerField(null=True)),
                ('time_left', models.IntegerField(null=True)),
                ('emp_assigned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DepInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(choices=[('Corporate', 'Corporate'), ('Finance', 'Finance'), ('Business Development', 'Business Development'), ('Human Resource', 'Human Resource'), ('Library', 'Library'), ('Document Control', 'Document Control'), ('Information Technology', 'Information Technology'), ('Planning', 'Planning'), ('Administration', 'Administration'), ('Process', 'Process'), ('Quality', 'Quality'), ('Mechanical', 'Mechanical'), ('Projects', 'Projects'), ('Instrumentation', 'Instrumentation'), ('Civil Structural', 'Civil Structural'), ('Procurement', 'Procurement'), ('Electrical', 'Electrical'), ('Piping', 'Piping')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('designation', models.CharField(choices=[('Office Boy', 'Office Boy'), ('Driver', 'Driver'), ('Draftman', 'Draftman'), ('Assistant', 'Assistant'), ('Sr Assistant', 'Sr Assistant'), ('Secreatary', 'Secreatary'), ('Executive', 'Executive'), ('Sr Executive', 'Sr Executive'), ('Engineer', 'Engineer'), ('Graduate Trainee', 'Graduate Trainee'), ('GTE', 'GTE'), ('Lead Engineer', 'Lead Engineer'), ('Sr Engineer', 'Sr Engineer'), ('Manager', 'Manager'), ('Assistant Manager', 'Assistant Manager'), ('Deputy Manager', 'Deputy Manager'), ('Sr Manager', 'Sr Manager'), ('Chief Manager', 'Chief Manager'), ('General Manager', 'General Manager'), ('AVP', 'AVP'), ('VP', 'VP'), ('DP', 'DP'), ('CEO', 'CEO'), ('CMD', 'CMD')], max_length=200, null=True)),
                ('location', models.CharField(choices=[('Delhi', 'Delhi'), ('Offshore', 'Offshore')], max_length=200, null=True)),
                ('service_type', models.CharField(choices=[('Regular', 'Regular'), ('Contract', 'Contract')], max_length=200, null=True)),
                ('extended_hours', models.BooleanField(default=False)),
                ('department_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.DepInfo')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_type', models.CharField(choices=[('OH', 'OH'), ('PA', 'PA')], max_length=200, null=True)),
                ('project_id', models.IntegerField(primary_key=True, serialize=False)),
                ('project_client', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('controlled_manhours', models.IntegerField(null=True)),
                ('completion_date', models.DateTimeField(null=True)),
                ('department_assigned', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('finished', models.BooleanField(default=False)),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Report_extended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('everyday_hours', models.CharField(max_length=100, null=True, validators=[django.core.validators.int_list_validator])),
                ('hours_reported', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('approved', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Activity')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('everyday_hours', models.CharField(max_length=100, null=True, validators=[django.core.validators.int_list_validator])),
                ('hours_reported', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('extended_hours', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Activity')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Project')),
            ],
        ),
        migrations.AddField(
            model_name='depinfo',
            name='department_hod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee'),
        ),
        migrations.AddField(
            model_name='department',
            name='assigned_to',
            field=models.ManyToManyField(to='accounts.Employee'),
        ),
        migrations.AddField(
            model_name='department',
            name='department_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.DepInfo'),
        ),
        migrations.AddField(
            model_name='department',
            name='project_assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Project'),
        ),
        migrations.AddField(
            model_name='activity',
            name='department_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.DepInfo'),
        ),
    ]
