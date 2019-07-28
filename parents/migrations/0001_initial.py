# Generated by Django 2.2.3 on 2019-07-23 10:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0002_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email_address', models.EmailField(blank=True, max_length=70)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.My_Students')),
            ],
        ),
    ]
