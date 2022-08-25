# Generated by Django 4.0.5 on 2022-08-25 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkuBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('company_name', models.CharField(blank=True, max_length=20, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('main_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.skubrand')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('qty', models.IntegerField(blank=True, default=0, null=True)),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Initial', 'Initial'), ('Assigned', 'Assigned'), ('Pending', 'Pending'), ('Complete', 'Complete')], default='Initial', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.sku')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.supplier')),
            ],
        ),
    ]
