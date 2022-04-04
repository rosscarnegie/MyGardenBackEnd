# Generated by Django 4.0.3 on 2022-04-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gardener',
            name='zone',
            field=models.CharField(blank=True, default=1, max_length=3, null=True, verbose_name='Your USDA Hardiness Zone'),
        ),
    ]