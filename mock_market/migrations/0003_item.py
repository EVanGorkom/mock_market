# Generated by Django 4.2.7 on 2023-11-30 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mock_market', '0002_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock_market.vendor')),
            ],
        ),
    ]
