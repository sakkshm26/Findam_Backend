# Generated by Django 4.0 on 2022-02-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findam', '0003_alter_cs_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='link',
            field=models.CharField(max_length=100),
        ),
    ]
