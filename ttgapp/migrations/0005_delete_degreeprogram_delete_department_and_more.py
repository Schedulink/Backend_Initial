# Generated by Django 4.2.6 on 2023-10-28 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttgapp', '0004_semester'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Degreeprogram',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
