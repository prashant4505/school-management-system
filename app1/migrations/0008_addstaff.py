# Generated by Django 3.2.4 on 2021-08-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210803_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='addStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('umail', models.CharField(max_length=50)),
                ('contact_num', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
