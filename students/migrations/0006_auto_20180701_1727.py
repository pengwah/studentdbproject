# Generated by Django 2.0.6 on 2018-07-02 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20180630_1618'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['fullname'], name='fullname_idx'),
        ),
    ]
