# Generated by Django 3.2.5 on 2021-07-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_auto_20210729_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overnight_stay',
            name='day',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='overnight_stay',
            name='month',
            field=models.IntegerField(),
        ),
    ]
