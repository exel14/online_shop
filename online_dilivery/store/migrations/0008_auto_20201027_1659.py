# Generated by Django 3.1.2 on 2020-10-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20201027_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(null=True, to='store.Tag'),
        ),
    ]
