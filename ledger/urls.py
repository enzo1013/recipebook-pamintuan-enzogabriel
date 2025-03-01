from django.urls import path
from .views import index, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='detail'),
]

app_name = 'ledger'