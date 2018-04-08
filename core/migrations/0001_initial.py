# Generated by Django 2.0.4 on 2018-04-08 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=15, verbose_name='Nome Cliente')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=15, verbose_name='Nome Produto')),
                ('descricao', models.TextField(max_length=50, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
            ],
        ),
    ]