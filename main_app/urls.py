from django.urls import path
from .views import ProductCreateView, GetAllShippedFoodPacks, GetAllScheduledFoodPacks, NumberOfShippedFoodPacks, GetFoodPacks, MakePickup


urlpatterns = [
    path('new_food_pack', ProductCreateView.as_view(), name='new_food_packs'),
    path('shipped_food_packs', GetAllShippedFoodPacks.as_view(), name='shipped_food_packs'),
    path('sheduled_food_packs', GetAllScheduledFoodPacks.as_view(), name='sheduled_food_packs'),
    path('number_of_shipped_food_packs', NumberOfShippedFoodPacks.as_view(), name='#shipped'),
    path('food_packs', GetFoodPacks.as_view(), name='available_for_pickup'),
    path('pickup', MakePickup.as_view(), name='pickup_food_pack'),
]