from django.urls import path
from .views import MealListCreateView,MealRetrieveUpdateDestroyView,MealByDateView,MealItemCreateView

urlpatterns = [
    path('meals/', MealListCreateView.as_view(), name='meal-list-create'),
    path('meals/<int:pk>/', MealRetrieveUpdateDestroyView.as_view(), name='meal-update-destroy'),
    path('meals/date/<str:date>/', MealByDateView.as_view(), name='meal-by-date'),
    path('meals/<meal_id>/items/', MealItemCreateView.as_view(), name='mealitem-create'),
]
