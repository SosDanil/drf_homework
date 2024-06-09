# Generated by Django 5.0.6 on 2024-06-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_method',
            field=models.CharField(choices=[('cash', 'Наличными'), ('transfer', 'Перевод на счет')], verbose_name='способ оплаты'),
        ),
    ]
