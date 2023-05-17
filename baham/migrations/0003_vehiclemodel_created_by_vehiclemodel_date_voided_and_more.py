# Generated by Django 4.2 on 2023-05-17 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baham', '0002_userprofile_remove_companion_user_ptr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclemodel',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_vehicle_models', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='date_voided',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='is_voided',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_vehicle_models', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='void_reason',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='voided_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='voided_vehicle_models', to=settings.AUTH_USER_MODEL),
        ),
    ]
