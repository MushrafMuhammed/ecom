# Generated by Django 4.1.4 on 2023-01-07 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('holder_name', models.CharField(max_length=25)),
                ('ifc_code', models.CharField(max_length=25)),
                ('bank_branch', models.CharField(max_length=25)),
                ('account_number', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='seller/')),
            ],
        ),
    ]
