# Generated by Django 3.0.8 on 2020-07-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FNDRest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faketext',
            name='feedback_one',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='faketext',
            name='feedback_two',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
