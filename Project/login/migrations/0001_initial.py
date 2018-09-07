# Generated by Django 2.1 on 2018-09-07 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=20)),
                ('customer_address', models.CharField(max_length=200)),
                ('customer_birthday', models.DateField()),
                ('customer_occupation', models.CharField(max_length=30)),
                ('customer_gender', models.CharField(max_length=1)),
            ],
        ),
    ]