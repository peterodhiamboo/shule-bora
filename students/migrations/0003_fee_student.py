# Generated by Django 2.2.3 on 2019-07-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='student',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
