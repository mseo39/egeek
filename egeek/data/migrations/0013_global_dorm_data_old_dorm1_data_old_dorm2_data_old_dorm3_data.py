# Generated by Django 3.2.4 on 2021-07-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20210720_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='global_dorm_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dorm', models.CharField(max_length=10)),
                ('dorm_number', models.CharField(max_length=10)),
                ('student_number', models.CharField(max_length=10)),
                ('qr_image', models.ImageField(null=True, upload_to='')),
                ('file_name', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='old_dorm1_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dorm', models.CharField(max_length=10)),
                ('dorm_number', models.CharField(max_length=10)),
                ('student_number', models.CharField(max_length=10)),
                ('qr_image', models.ImageField(null=True, upload_to='')),
                ('file_name', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='old_dorm2_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dorm', models.CharField(max_length=10)),
                ('dorm_number', models.CharField(max_length=10)),
                ('student_number', models.CharField(max_length=10)),
                ('qr_image', models.ImageField(null=True, upload_to='')),
                ('file_name', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='old_dorm3_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dorm', models.CharField(max_length=10)),
                ('dorm_number', models.CharField(max_length=10)),
                ('student_number', models.CharField(max_length=10)),
                ('qr_image', models.ImageField(null=True, upload_to='')),
                ('file_name', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
