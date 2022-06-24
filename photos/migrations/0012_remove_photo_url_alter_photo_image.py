# Generated by Django 4.0.3 on 2022-06-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_alter_photo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]