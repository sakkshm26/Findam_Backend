# Generated by Django 4.0 on 2022-02-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cs',
            name='link',
            field=models.CharField(default='abc', max_length=50),
        ),
    ]
