# Generated by Django 3.1 on 2020-12-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threeknots', '0032_quotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='customeri',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
