from django.contrib.auth.models import User
from django.db import models


# Create your models here
class WeightMeasurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField()
    weight = models.FloatField()  

    def __str__(self):
        return f"{self.user.username}'s Weight on {self.date}"


class Food(models.Model):
    id=models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=100.00)
    calories = models.IntegerField(default=0)
    fat = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    carbohydrates = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    
class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE, default=0)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"Profile - Age: {self.age}, Weight: {self.weight}, Height: {self.height}, Gender: {self.get_gender_display()}"
class BMRMeasurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bmr = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BMR Measurement for {self.user.username} at {self.timestamp}"

    