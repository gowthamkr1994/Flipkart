# Generated by Django 2.1.7 on 2019-03-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190323_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='contact',
            field=models.CharField(default='', max_length=12),
        ),
    ]
