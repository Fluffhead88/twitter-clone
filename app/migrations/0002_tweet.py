# Generated by Django 2.0.6 on 2018-06-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(default='No tweet body provided', max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
