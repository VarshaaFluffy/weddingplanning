# Generated by Django 3.1 on 2020-12-02 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threeknots', '0027_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_on', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threeknots.user')),
                ('vendorty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threeknots.vendor')),
            ],
        ),
    ]
