# Generated by Django 2.2.6 on 2019-12-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(default='xixi.jpg', upload_to='images/'),
        ),
    ]