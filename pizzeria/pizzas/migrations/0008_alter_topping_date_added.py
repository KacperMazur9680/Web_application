# Generated by Django 4.0.6 on 2022-07-30 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0007_alter_topping_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]