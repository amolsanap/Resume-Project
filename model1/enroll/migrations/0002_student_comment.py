# Generated by Django 3.1.6 on 2021-02-21 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='Not Available', max_length=40),
        ),
    ]
