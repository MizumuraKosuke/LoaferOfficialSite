# Generated by Django 2.0.3 on 2018-05-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0002_auto_20180417_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live',
            name='adv',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='artists',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='door',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='live',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
