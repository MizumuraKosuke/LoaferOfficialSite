# Generated by Django 2.0.3 on 2018-05-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20180417_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='onair_time',
        ),
        migrations.AddField(
            model_name='media',
            name='Category',
            field=models.CharField(choices=[('TV', 'TV'), ('Radio', 'Radio'), ('Magazine', 'Magazine'), ('Web', 'Web'), ('Other', 'Other')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='broadcast',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='explain',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]