from django.urls import path
from .views import index, RecipeListView, RecipeCreateView, RecipeUpdateView, RecipeImageCreateView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipeListView.as_view(), name='list'),
    path('recipe/add', RecipeCreateView.as_view(), name='create'),
    path('recipe/<int:pk>', RecipeUpdateView.as_view(), name='detail'),
    path('recipe/<int:pk>/add_image', RecipeImageCreateView.as_view())
]

app_name = 'ledger'