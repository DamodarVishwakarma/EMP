# Generated by Django 4.0.6 on 2022-08-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_employeeattendance_note'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeattendance',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='note',
            field=models.CharField(max_length=200),
        ),
    ]