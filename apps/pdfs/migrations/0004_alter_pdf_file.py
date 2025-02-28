# Generated by Django 4.0.6 on 2022-08-03 21:19

import apps.common.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfs', '0003_alter_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='file',
            field=models.FileField(upload_to='media/pdfs/', validators=[apps.common.custom_validators.validate_pdf_file_type]),
        ),
    ]
