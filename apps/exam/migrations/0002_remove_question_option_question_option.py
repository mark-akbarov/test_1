# Generated by Django 4.1.3 on 2022-12-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='option',
        ),
        migrations.AddField(
            model_name='question',
            name='option',
            field=models.ManyToManyField(to='exam.option'),
        ),
    ]