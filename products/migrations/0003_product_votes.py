# Generated by Django 2.2.6 on 2019-12-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191211_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='votes',
            field=models.IntegerField(default=1),
        ),
    ]
