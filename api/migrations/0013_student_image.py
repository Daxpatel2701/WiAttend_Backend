# Generated by Django 4.1.12 on 2023-10-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_attendance_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
