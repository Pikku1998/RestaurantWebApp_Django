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


class ItemDetail(DetailView):
    model = Item
    template_name = 'item_detail.html'


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
