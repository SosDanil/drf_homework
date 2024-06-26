# Generated by Django 5.0.6 on 2024-06-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_payment_pay_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='sum',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id_сессии'),
        ),
    ]
