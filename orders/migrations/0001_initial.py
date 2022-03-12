# Generated by Django 4.0.2 on 2022-03-12 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Дата заказа')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='caps.basket')),
            ],
            options={
                'verbose_name': 'Товар заказа',
                'verbose_name_plural': 'Товары заказов',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30, verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статус заказов',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=100, verbose_name='Код заказа')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('send_date', models.DateField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]