# Generated by Django 4.0.10 on 2023-06-01 10:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCode',
            fields=[
                ('sub_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=50, null=True)),
                ('sem', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)])),
                ('scheme', models.CharField(choices=[('18th SCHEME', '18th SCHEME'), ('16th SCHEME', '16th SCHEME'), ('21th SCHEME', '21th SCHEME')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('date', models.DateField(null=True)),
                ('questionPaper', models.FileField(null=True, upload_to='pdf/question_papers/', verbose_name='Pdf')),
                ('sub_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base1.subcode')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='images/gux+cat.svg', upload_to='images/')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ideal_index', models.IntegerField(blank=True, null=True)),
                ('upload_date', models.DateField(auto_now_add=True, null=True)),
                ('note', models.FileField(null=True, upload_to='pdf/notes/', verbose_name='Pdf')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base1.professor')),
                ('sub_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base1.subcode')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('l_submission', models.DateTimeField(blank=True, null=True)),
                ('assignment', models.FileField(null=True, upload_to='pdf/assignments/', verbose_name='Pdf')),
                ('prof', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base1.professor')),
                ('sub_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base1.subcode')),
            ],
        ),
    ]
