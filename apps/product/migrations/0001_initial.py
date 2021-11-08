# Generated by Django 3.2.9 on 2021-11-07 19:48

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Название товара')),
                ('photo', models.CharField(max_length=200, verbose_name='Фото file_id')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('category_code', models.CharField(max_length=20, verbose_name='Код категории')),
                ('category_name', models.CharField(max_length=20, verbose_name='Название категории')),
                ('subcategory_code', models.CharField(max_length=20, verbose_name='Код подкатегории')),
                ('subcategory_name', models.CharField(max_length=20, verbose_name='Название подкатегории')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость')),
                ('purchase_time', models.DateTimeField(auto_now_add=True, verbose_name='Время покупки')),
                ('shipping_address', jsonfield.fields.JSONField(null=True, verbose_name='Адрес доставки')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='Email')),
                ('receiver', models.CharField(max_length=100, null=True, verbose_name='Имя получателя')),
                ('successful', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('buyer', models.ForeignKey(on_delete=models.SET(0), to='account.user', verbose_name='Покупатель')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
    ]
