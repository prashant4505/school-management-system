# Generated by Django 3.2.4 on 2021-07-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
