# Generated by Django 3.1 on 2020-11-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threeknots', '0018_auto_20201124_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invi',
            name='list',
            field=models.CharField(max_length=100),
        ),
    ]
