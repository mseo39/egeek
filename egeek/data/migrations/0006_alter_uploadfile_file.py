# Generated by Django 3.2.4 on 2021-07-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='file/'),
        ),
    ]
