# Generated by Django 3.0.3 on 2020-04-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200428_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='emp_assigned',
            field=models.BooleanField(default=False),
        ),
    ]
