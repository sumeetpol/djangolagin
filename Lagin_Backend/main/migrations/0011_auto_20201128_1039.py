# Generated by Django 3.0.6 on 2020-11-28 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201128_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainsignup',
            name='image1',
            field=models.ImageField(null=True, upload_to='imgmulti'),
        ),
        migrations.AddField(
            model_name='mainsignup',
            name='image2',
            field=models.ImageField(null=True, upload_to='imgmulti'),
        ),
    ]
