# Generated by Django 5.1.1 on 2024-10-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]