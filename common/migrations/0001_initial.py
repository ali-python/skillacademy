# Generated by Django 3.1.2 on 2020-10-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('father_name', models.CharField(blank=True, max_length=200, null=True)),
                ('cnic', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('course_study', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=13, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('status_not_sure', models.CharField(blank=True, max_length=13, null=True)),
                ('status_intro_class', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
    ]
