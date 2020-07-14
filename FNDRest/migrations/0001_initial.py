# Generated by Django 3.0.8 on 2020-07-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fake_text', models.TextField()),
                ('feedback_one', models.CharField(blank=True, default='', max_length=200)),
                ('feedback_two', models.CharField(blank=True, default='', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
