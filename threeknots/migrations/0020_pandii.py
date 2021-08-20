# Generated by Django 3.1 on 2020-11-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threeknots', '0019_auto_20201124_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='pandii',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=58)),
                ('address', models.CharField(max_length=58)),
                ('experi', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('service', models.CharField(max_length=100)),
                ('lang', models.CharField(max_length=100, null=True)),
                ('about', models.TextField(max_length=98)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]