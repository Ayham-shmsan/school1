# Generated by Django 5.1.4 on 2024-12-28 23:09

import attendances.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0003_attendance_section'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='section',
            field=models.ForeignKey(default=attendances.models.get_default_section, on_delete=django.db.models.deletion.CASCADE, to='school.section', verbose_name='الشعبة'),
        ),
    ]
