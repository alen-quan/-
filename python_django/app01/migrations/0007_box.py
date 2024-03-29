# Generated by Django 4.0.2 on 2022-04-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_alter_proinfo_ways'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manage_area', models.CharField(blank=True, max_length=255, null=True, verbose_name='管理区域')),
                ('box_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='光交接箱名称')),
                ('box_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='光交接箱类型')),
                ('terminal_n', models.CharField(blank=True, max_length=255, null=True, verbose_name='总端子数')),
                ('terminal_f', models.CharField(blank=True, max_length=255, null=True, verbose_name='空闲端子数')),
                ('core_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='主干光缆名称')),
                ('optical_direction', models.CharField(blank=True, max_length=255, null=True, verbose_name='光纤方向')),
                ('totle_wick', models.CharField(blank=True, max_length=255, null=True, verbose_name='总芯数')),
                ('available', models.CharField(blank=True, max_length=255, null=True, verbose_name='空闲')),
                ('occupancy', models.CharField(blank=True, max_length=255, null=True, verbose_name='占用')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='地址')),
            ],
            options={
                'db_table': 'box',
                'managed': True,
            },
        ),
    ]
