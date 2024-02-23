from django.contrib import admin
from .models import  WeightMeasurement,Food,FoodLog,UserProfile,BMRMeasurement
# Register your models here.

admin.site.register(WeightMeasurement)
admin.site.register(Food)
admin.site.register(FoodLog)
admin.site.register(UserProfile)
admin.site.register(BMRMeasurement)