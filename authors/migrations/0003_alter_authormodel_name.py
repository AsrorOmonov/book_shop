# Generated by Django 3.2.4 on 2021-06-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20210626_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authormodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]
