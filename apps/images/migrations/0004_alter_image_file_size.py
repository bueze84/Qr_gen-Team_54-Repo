# Generated by Django 4.0.6 on 2022-08-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_file_alter_image_qr_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file_size',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
