# Generated by Django 4.2.6 on 2023-11-04 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttgapp', '0020_alter_timetabledata_sub_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetabledata',
            name='sub_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttgapp.subject'),
        ),
    ]
