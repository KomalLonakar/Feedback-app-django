# Generated by Django 3.1.4 on 2021-03-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0005_auto_20210321_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.TextField()),
                ('feedback', models.TextField()),
            ],
        ),
    ]
