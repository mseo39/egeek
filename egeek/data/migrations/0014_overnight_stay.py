# Generated by Django 3.2.4 on 2021-07-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_global_dorm_data_old_dorm1_data_old_dorm2_data_old_dorm3_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='overnight_stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('student_number', models.IntegerField(max_length=8)),
                ('dorm', models.CharField(max_length=10)),
                ('dorm_number', models.CharField(max_length=10)),
            ],
        ),
    ]