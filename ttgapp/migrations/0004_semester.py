# Generated by Django 4.2.6 on 2023-10-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttgapp', '0003_alter_degreeprogram_dept_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_id', models.IntegerField()),
                ('sem_num', models.IntegerField()),
                ('Deg_name', models.CharField(max_length=40)),
                ('Reg_year', models.IntegerField()),
            ],
        ),
    ]
