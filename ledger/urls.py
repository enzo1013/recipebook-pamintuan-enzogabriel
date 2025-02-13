from django.urls import path
from .views import index, recipeList, recipeOne, recipeTwo

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipeList, name='list'),
    path('recipe/1', recipeOne, name='1'),
    path('recipe/2', recipeTwo, name='2')
]

app_name = 'ledger'