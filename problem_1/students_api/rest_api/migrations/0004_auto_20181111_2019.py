# Generated by Django 2.0.9 on 2018-11-12 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_student_enrolled_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrolled_to',
            field=models.ManyToManyField(blank=True, null=True, to='rest_api.Class'),
        ),
    ]
