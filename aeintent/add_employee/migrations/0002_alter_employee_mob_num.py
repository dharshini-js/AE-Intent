# Generated by Django 5.1.4 on 2024-12-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mob_num',
            field=models.CharField(max_length=10),
        ),
    ]