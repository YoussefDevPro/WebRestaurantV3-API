# Generated by Django 5.0.7 on 2024-07-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('ingredients', models.CharField(max_length=5000)),
                ('prix', models.FloatField(default=0)),
                ('prix_XXL', models.FloatField(default=0)),
                ('vegetarienne', models.BooleanField(default=False)),
                ('disponibilite', models.BooleanField(default=True)),
                ('image_link', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('ingredients', models.CharField(max_length=5000)),
                ('prix', models.FloatField(default=0)),
                ('disponibilite', models.BooleanField(default=True)),
                ('image_link', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_products', models.TextField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('ingredients', models.CharField(max_length=5000)),
                ('prix_petite', models.FloatField(default=0)),
                ('prix', models.FloatField(default=0)),
                ('prix_grand', models.FloatField(default=0)),
                ('vegetarienne', models.BooleanField(default=False)),
                ('disponibilite', models.BooleanField(default=True)),
                ('image_link', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('ingredients', models.CharField(max_length=5000)),
                ('prix', models.FloatField(default=0)),
                ('vegetarienne', models.BooleanField(default=False)),
                ('disponibilite', models.BooleanField(default=True)),
                ('image_link', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('guests', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('ingredients', models.CharField(max_length=5000)),
                ('prix', models.FloatField(default=0)),
                ('prix_XXL', models.FloatField(default=0)),
                ('vegetarienne', models.BooleanField(default=False)),
                ('disponibilite', models.BooleanField(default=True)),
                ('image_link', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('prix', models.FloatField(default=0)),
                ('disponibilite', models.BooleanField(default=True)),
                ('image_link', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Tacos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('ingredients', models.CharField(max_length=5000)),
                ('prix', models.FloatField(default=0)),
                ('prix_XXL', models.FloatField(default=0)),
                ('vegetarienne', models.BooleanField(default=False)),
                ('disponibilite', models.BooleanField(default=True)),
                ('image_link', models.CharField(max_length=10000)),
            ],
        ),
    ]
