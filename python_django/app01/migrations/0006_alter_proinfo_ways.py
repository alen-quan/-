# Generated by Django 4.0.2 on 2022-04-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_alter_proinfo_fixed_alter_proinfo_tiao_km_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proinfo',
            name='ways',
            field=models.IntegerField(verbose_name='敷设方式'),
        ),
    ]
