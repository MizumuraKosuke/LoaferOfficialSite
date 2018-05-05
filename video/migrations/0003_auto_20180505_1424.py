# Generated by Django 2.0.3 on 2018-05-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20180416_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='URL',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='explain',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]