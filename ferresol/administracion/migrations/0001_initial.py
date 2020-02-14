# Generated by Django 3.0.3 on 2020-02-13 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_total', models.FloatField()),
                ('cantidad_productos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CuentaBancaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=45)),
                ('precio', models.IntegerField()),
                ('tipo', models.CharField(blank=True, default='', max_length=45)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_recepcionista', models.CharField(blank=True, default='', max_length=45)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('direccion', models.CharField(blank=True, default='', max_length=45)),
                ('distrito', models.CharField(blank=True, default='', max_length=45)),
                ('provincia', models.CharField(blank=True, default='', max_length=45)),
                ('departamento', models.CharField(blank=True, default='', max_length=45)),
                ('nombre_comprador', models.CharField(blank=True, default='', max_length=45)),
                ('id_cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Cotizacion')),
                ('id_cuenta_bancaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.CuentaBancaria')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Producto')),
            ],
        ),
    ]
