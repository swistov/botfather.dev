# Generated by Django 3.2.9 on 2021-11-07 19:18

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_id', models.BigIntegerField(default=1, unique=True, verbose_name='ID пользователя')),
                ('name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('username', models.CharField(max_length=100, verbose_name='Username пользователя')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('referrer', models.BigIntegerField(verbose_name='Реферал ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'verbose_name': 'Реферал',
                'verbose_name_plural': 'Рефералы',
            },
        ),
    ]
