from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, MEAL_TYPE


class MenuList(ListView):
    queryset = Item.objects.all()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # gets item_list from super class ListView
        context['category'] = MEAL_TYPE
        return context

