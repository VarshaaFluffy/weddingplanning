# Generated by Django 3.1 on 2020-11-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threeknots', '0010_auto_20201120_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
