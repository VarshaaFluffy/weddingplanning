# Generated by Django 3.1 on 2020-12-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threeknots', '0049_carty_tamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]