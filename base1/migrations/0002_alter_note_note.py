# Generated by Django 4.0.10 on 2023-06-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.FileField(blank=True, null=True, upload_to='pdf/notes/', verbose_name='Pdf'),
        ),
    ]
