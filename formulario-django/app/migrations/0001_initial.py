# Generated by Django 4.0.3 on 2022-04-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('unidade_medida', models.CharField(choices=[('Metros', 'MT'), ('Unidade', 'UN'), ('Metro Cubico', 'M3'), ('Metro Quadrado', 'M2'), ('Quilo', 'KG'), ('Tonelada', 'TO'), ('Conjunto', 'CJ'), ('Peça', 'PC'), ('Pacote', 'PT')], max_length=14, verbose_name='Unidade de Medida')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Quantidade')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('data_entrada', models.DateTimeField()),
            ],
        ),
    ]
