# Generated by Django 3.1 on 2020-11-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threeknots', '0003_pets'),
    ]

    operations = [
        migrations.CreateModel(
            name='venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=58)),
                ('type', models.CharField(max_length=58)),
                ('address', models.CharField(max_length=58)),
                ('hallsize', models.CharField(max_length=58)),
                ('seats', models.IntegerField(max_length=58)),
                ('rooms', models.IntegerField(max_length=58)),
                ('number', models.IntegerField(max_length=58)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='pets',
        ),
    ]
