# Generated by Django 2.0.1 on 2018-01-04 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arbitrage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pair', to='arbitrage.Coin'),
        ),
    ]
