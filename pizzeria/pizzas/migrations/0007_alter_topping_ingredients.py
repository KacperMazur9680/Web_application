# Generated by Django 4.0.6 on 2022-07-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_alter_pizza_order_alter_topping_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='ingredients',
            field=models.TextField(default=''),
        ),
    ]