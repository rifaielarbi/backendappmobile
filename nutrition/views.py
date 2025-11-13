from rest_framework import generics, permissions
from .models import Meal, MealItem
from .mealserializer import MealSerializer, mealitemserializer
from rest_framework.exceptions import PermissionDenied


# Créer / Lister les repas
class MealListCreateView(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Modifier / Supprimer un repas existant
class MealRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

class MealByDateView(generics.ListAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        date = self.kwargs['date']
        return Meal.objects.filter(user=self.request.user, date=date)
    
class MealItemCreateView(generics.ListCreateAPIView):
    serializer_class = mealitemserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MealItem.objects.filter(meal__user=self.request.user)

    def perform_create(self, serializer):
        meal_id = self.kwargs.get('meal_id')
        try:
            meal = Meal.objects.get(id=meal_id)
            print("Meal ID récupéré :", meal_id)
        except Meal.DoesNotExist:
            raise PermissionDenied("Meal does not exist")
        if meal.user != self.request.user:
            raise PermissionDenied("You do not have permission to add items to this meal.")
        serializer.save(meal=meal)