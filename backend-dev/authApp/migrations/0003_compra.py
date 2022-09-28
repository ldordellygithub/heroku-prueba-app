# Generated by Django 4.1.1 on 2022-09-28 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_v', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField()),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.clientes')),
            ],
        ),
    ]