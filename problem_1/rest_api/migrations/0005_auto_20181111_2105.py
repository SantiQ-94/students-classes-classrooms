# Generated by Django 2.0.9 on 2018-11-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_auto_20181111_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrolled_to',
            field=models.ManyToManyField(blank=True, null=True, related_name='enrolled_students', to='rest_api.Class'),
        ),
    ]
