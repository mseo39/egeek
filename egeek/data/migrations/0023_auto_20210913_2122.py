# Generated by Django 3.2.5 on 2021-09-13 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_qrfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrfile',
            name='chk',
        ),
        migrations.RemoveField(
            model_name='qrfile',
            name='title',
        ),
    ]
