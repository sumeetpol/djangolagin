# Generated by Django 3.1.4 on 2020-12-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_fav_list_heartcolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fav_list',
            name='heartcolor',
        ),
        migrations.AddField(
            model_name='mainsignup',
            name='heartc',
            field=models.TextField(default='hearto'),
        ),
    ]
