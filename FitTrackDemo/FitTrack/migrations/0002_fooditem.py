# Generated by Django 5.0.1 on 2024-02-02 03:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FitTrack', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.FloatField()),
                ('Carbohydrates', models.FloatField()),
                ('Cholesterol', models.FloatField()),
                ('Saturated_fat', models.FloatField()),
                ('Total_Fat', models.FloatField()),
                ('Fiber_Content', models.FloatField()),
                ('Potassium', models.FloatField()),
                ('Protein', models.FloatField()),
                ('Sodium', models.FloatField()),
                ('Sugar', models.FloatField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
