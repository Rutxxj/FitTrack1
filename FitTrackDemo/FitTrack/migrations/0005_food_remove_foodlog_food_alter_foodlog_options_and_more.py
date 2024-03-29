# Generated by Django 5.0.1 on 2024-02-04 03:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FitTrack', '0004_remove_fooditem_users_alter_foodlog_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('quantity', models.DecimalField(decimal_places=2, default=100.0, max_digits=7)),
                ('calories', models.IntegerField(default=0)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('carbohydrates', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='foodlog',
            name='food',
        ),
        migrations.AlterModelOptions(
            name='foodlog',
            options={'verbose_name': 'Food Log', 'verbose_name_plural': 'Food Log'},
        ),
        migrations.RemoveField(
            model_name='foodlog',
            name='date',
        ),
        migrations.AlterField(
            model_name='foodlog',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodlog',
            name='food_consumed',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FitTrack.food'),
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
    ]
