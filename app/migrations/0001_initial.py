# Generated by Django 4.2.3 on 2023-07-08 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField(max_length=15)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=20)),
                ('vehicle', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('model_year', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('make', models.CharField(max_length=50)),
                ('engine_power', models.CharField(max_length=50)),
                ('engine_type', models.CharField(max_length=100)),
                ('engine_power_torque', models.CharField(max_length=50)),
                ('top_speed', models.PositiveIntegerField()),
                ('fuel_economy', models.CharField(max_length=50)),
                ('fuel_type', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='bikes/')),
                ('mileage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('engine_displacement', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payload_capacity', models.CharField(max_length=50)),
                ('battery', models.CharField(max_length=50)),
                ('additional_options_features', models.TextField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('colors', models.ManyToManyField(to='app.color')),
            ],
        ),
    ]
