# Generated by Django 2.0.3 on 2018-05-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0005_auto_20180505_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livecontact',
            name='which_live',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
