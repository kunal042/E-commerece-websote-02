# Generated by Django 4.1.5 on 2023-02-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='otp',
            field=models.IntegerField(default=8898898),
        ),
    ]
