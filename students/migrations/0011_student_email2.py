# Generated by Django 2.0.6 on 2018-07-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20180715_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email2',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]