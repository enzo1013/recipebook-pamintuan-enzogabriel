from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    page_title = 'Recipe List'
    template_name = 'list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    page_title = 'Recipe <int:pk>'
    template_name = 'detail.html'

def index(request):
    return HttpResponse('Hello world! Go to /recipes/list to begin.')