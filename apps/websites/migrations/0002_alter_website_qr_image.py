# Generated by Django 4.0.6 on 2022-08-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='qr_image',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes'),
        ),
    ]
