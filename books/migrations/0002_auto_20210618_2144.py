# Generated by Django 3.2.4 on 2021-06-18 21:44

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='isbn',
            field=models.CharField(max_length=13, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='page_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]