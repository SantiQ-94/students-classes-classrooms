# Generated by Django 2.0.9 on 2018-11-11 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='enrolled_to',
            field=models.ManyToManyField(to='rest_api.Class'),
        ),
    ]
