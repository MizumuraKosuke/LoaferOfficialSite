# Generated by Django 2.0.3 on 2018-05-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20180503_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='imagesub',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
