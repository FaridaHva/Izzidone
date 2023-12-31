# Generated by Django 3.2.20 on 2023-08-25 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_auto_20230825_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='Street Address')),
                ('start_date', models.DateTimeField(verbose_name='Select Start Date')),
                ('starting_time', models.DateTimeField(verbose_name='Select Starting Time')),
                ('service_detail', models.TextField(verbose_name='Service Details')),
                ('upload_image', models.ImageField(upload_to='', verbose_name='Upload Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('price', models.IntegerField(default=0, verbose_name='Total Price')),
                ('options', models.ManyToManyField(to='services.AllPros', verbose_name='Options')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.professional', verbose_name='Professional')),
                ('subService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subservice_orders', to='services.subservice', verbose_name='Subservice')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title_orders', to='services.subservice', verbose_name='Title')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
