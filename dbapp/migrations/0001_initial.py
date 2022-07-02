# Generated by Django 3.2.12 on 2022-05-24 00:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('ssn', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('specialty', models.CharField(choices=[('أسنان', 'أسنان'), ('أنف وأذن وحنجرة', 'أنف وأذن وحنجرة'), ('قلب', 'قلب'), ('نساء', 'نساء'), ('باطني', 'باطني'), ('أطفال', 'أطفال'), ('توليد', 'توليد'), ('جلد', 'جلد'), ('الجهاز البولي', 'الجهاز البولي'), ('الجهاز العصبي', 'الجهاز العصبي'), ('الجهاز الهضمي', 'الجهاز الهضمي'), ('رئة', 'رئة'), ('غدد', 'غدد'), ('جراحة', 'جراحة'), ('عظام', 'عظام'), ('جراحة عظام', 'جراحة عظام')], max_length=30)),
                ('current_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(max_length=20, unique=True)),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('ذكر', 'ذكر'), ('انثى', 'انثى'), ('اخر', 'اخر'), ('غير محدد', 'غير محدد')], default='غير محدد', max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('current_address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_id', models.CharField(max_length=20, unique=True, verbose_name='appointment id')),
                ('active', models.BooleanField(default=True)),
                ('app_type', models.CharField(choices=[('أسنان', 'أسنان'), ('أنف وأذن وحنجرة', 'أنف وأذن وحنجرة'), ('قلب', 'قلب'), ('نساء', 'نساء'), ('باطني', 'باطني'), ('أطفال', 'أطفال'), ('توليد', 'توليد'), ('جلد', 'جلد'), ('الجهاز البولي', 'الجهاز البولي'), ('الجهاز العصبي', 'الجهاز العصبي'), ('الجهاز الهضمي', 'الجهاز الهضمي'), ('رئة', 'رئة'), ('غدد', 'غدد'), ('جراحة', 'جراحة'), ('عظام', 'عظام'), ('جراحة عظام', 'جراحة عظام')], max_length=30)),
                ('app_date', models.DateField()),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('appoint_book_time', models.DateField(default=datetime.datetime.now)),
                ('d_name', models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.DO_NOTHING, to='dbapp.doctor', verbose_name="Doctor's name")),
                ('p_name', models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.DO_NOTHING, to='dbapp.patient', verbose_name="Patient's name")),
            ],
        ),
    ]