# Generated by Django 3.2 on 2022-09-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obj2app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detect',
            name='ifile',
            field=models.FileField(upload_to='uploads/documents/'),
        ),
    ]