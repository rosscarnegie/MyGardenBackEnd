# Generated by Django 4.0.3 on 2022-04-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_gardener_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardener',
            name='zone',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Your USDA Hardiness Zone'),
        ),
    ]