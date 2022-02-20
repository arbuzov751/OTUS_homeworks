from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from menu.models import Menu


# def menu_list(request):
#     menu = Menu.objects.all()
#     context = {
#         "products": menu
#     }
#     return render(request, 'menu/menu_list.html', context=context)


class MenuListView(ListView):
    model = Menu


class MenuListDetailView(DetailView):
    model = Menu
    fields = "__all__"


class MenuCreateView(CreateView):
    model = Menu
    success_url = reverse_lazy('menu:menu_list')
    fields = '__all__'


class MenuUpdateView(UpdateView):
    model = Menu
    success_url = reverse_lazy('menu:menu_list')
    fields = '__all__'


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy('menu:menu_list')
    fields = '__all__'
