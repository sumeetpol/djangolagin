# Generated by Django 3.0.6 on 2020-11-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201128_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fav_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.BigIntegerField(null=True)),
                ('statusid', models.BigIntegerField(null=True)),
            ],
        ),
    ]