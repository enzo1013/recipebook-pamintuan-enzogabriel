from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello world! Go to /recipes/list to begin.')

def recipeList(request):
    context = {
        "recipes": [
            {
                "name": "Recipe 1",
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "link": "/recipe/2"
            }
        ]
    }
    return (render(request, 'list.html', context))

def recipeOne(request):
    context = {
            "name": "Recipe 1",
            "ingredients": [
            {
                "name": "tomato",
                "quantity": "3pcs"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "pork",
                "quantity": "1kg"
            },
            {
                "name": "water",
                "quantity": "1L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
        "link": "/recipe/1"
    }
    return (render(request, '1.html', context))

def recipeTwo(request):
    context = {
        "name": "Recipe 2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
        "link": "/recipe/2"
    }
    return (render(request, '2.html', context))