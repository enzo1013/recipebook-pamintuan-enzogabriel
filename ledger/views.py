from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recipe'] = Recipe.objects.all()
        ctx['form'] = RecipeForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset()
            ctx = self.get_context_data(**kwargs)
            ctx['form'] = form
            return self.return_to_response(ctx)

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'detail.html'

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create.html'

class RecipeImageCreateView(CreateView):
    model = Recipe
    form_class = RecipeImageForm
    template_name = 'create.html'

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'detail.html'

def index(request):
    return HttpResponse('Hello world! Go to /recipes/list to begin.')