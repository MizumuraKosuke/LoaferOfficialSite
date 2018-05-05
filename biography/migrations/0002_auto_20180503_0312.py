# Generated by Django 2.0.3 on 2018-05-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
