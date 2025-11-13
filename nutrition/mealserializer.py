from rest_framework import serializers
from .models import Meal, MealItem



class mealitemserializer(serializers.ModelSerializer):
    class Meta:
        model = MealItem
        fields = ['id', 'name', 'quantity_in_grams', 'calories_per_100g', 'protein_per_100g', 'carbohydrates_per_100g', 'fats_per_100g']
        
    
    
class MealSerializer(serializers.ModelSerializer):
    totals = serializers.SerializerMethodField()
    class Meta:
        model = Meal
        fields = ['id', 'name', 'quantity', 'date', 'time','totals']
    
    def get_totals(self, obj):
        return obj.total_nutrition()      