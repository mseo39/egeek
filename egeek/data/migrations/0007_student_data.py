# Generated by Django 3.2.4 on 2021-07-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_uploadfile_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dorm', models.CharField(max_length=10)),
                ('dorm_number', models.CharField(max_length=10)),
                ('student_number', models.CharField(max_length=10)),
            ],
        ),
    ]
