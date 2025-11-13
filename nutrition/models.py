from django.db import models
from users.models import User 
from django.conf import settings


class Meal(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='meals')
    name = models.CharField(max_length=255)
    quantity = models.FloatField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

    def total_nutrition(self):
        items = self.items.all()
        return {
            'calories': sum(item.total_calories() for item in items),
            'protein': sum(item.total_protein() for item in items),
            'carbohydrates': sum(item.total_carbohydrates() for item in items),
            'fats': sum(item.total_fats() for item in items),
        }


class MealItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255, default='')
    quantity_in_grams = models.FloatField()
    
    calories_per_100g = models.FloatField(default=0)
    protein_per_100g = models.FloatField(default=0)
    carbohydrates_per_100g = models.FloatField(default=0)
    fats_per_100g = models.FloatField(default=0)
    
    def total_calories(self):
        return (self.calories_per_100g * self.quantity_in_grams) / 100

    def total_protein(self):
        return (self.protein_per_100g * self.quantity_in_grams) / 100

    def total_carbohydrates(self):
        return (self.carbohydrates_per_100g * self.quantity_in_grams) / 100

    def total_fats(self):
        return (self.fats_per_100g * self.quantity_in_grams) / 100

    def __str__(self):
        return f"{self.quantity_in_grams}g of {self.name}"
