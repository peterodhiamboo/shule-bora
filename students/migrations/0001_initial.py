# Generated by Django 2.2.3 on 2019-07-06 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_class', '0003_auto_20190616_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_image', models.ImageField(upload_to='student_images/')),
                ('sur_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('ups_number', models.CharField(max_length=5)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=10)),
                ('student_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_class.Class_Layout')),
            ],
        ),
    ]
