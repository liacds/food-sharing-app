from django.urls import path
from .views import ProductCreateView


urlpatterns = [
    path('/new_food_pack', ProductCreateView.as_view(), name='register'),

]