# Generated by Django 3.2.4 on 2021-08-01 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='uid',
        ),
    ]
