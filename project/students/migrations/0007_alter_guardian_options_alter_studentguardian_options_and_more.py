# Generated by Django 5.1.4 on 2024-12-31 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('students', '0006_alter_studentsection_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guardian',
            options={'verbose_name': 'إدارة أولياء الأمور', 'verbose_name_plural': 'إدارة أولياء الأمور'},
        ),
        migrations.AlterModelOptions(
            name='studentguardian',
            options={'verbose_name': 'ولي الأمر', 'verbose_name_plural': 'أولياء الأمور'},
        ),
        migrations.AlterModelOptions(
            name='studentsection',
            options={'verbose_name': 'شعبة', 'verbose_name_plural': 'الشعب'},
        ),
        migrations.CreateModel(
            name='StudentAcademicRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False, verbose_name='هل تم التأكيد')),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.academicyear', verbose_name='السنة الأكادمية')),
                ('class_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.classlevel', verbose_name='الصف')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='الطالب')),
            ],
            options={
                'verbose_name': 'سجل دراسي',
                'verbose_name_plural': 'سجلات دراسية',
                'unique_together': {('student', 'academic_year', 'class_level')},
            },
        ),
    ]
