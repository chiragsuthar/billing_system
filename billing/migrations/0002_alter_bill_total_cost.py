# Generated by Django 5.0.4 on 2024-05-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
