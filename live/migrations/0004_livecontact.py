# Generated by Django 2.0.3 on 2018-05-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0003_auto_20180503_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('mail_address', models.EmailField(max_length=254, null=True)),
                ('which_live', models.CharField(choices=[('クリープハイプのすべて', 'クリープハイプのすべて'), ('パンツ', 'パンツ'), ('阿蘇ロックフェスティバル2018', '阿蘇ロックフェスティバル2018')], max_length=200, null=True)),
                ('ticket', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
