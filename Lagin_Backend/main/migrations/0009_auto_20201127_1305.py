# Generated by Django 3.0.6 on 2020-11-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201126_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsignup',
            name='age',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
