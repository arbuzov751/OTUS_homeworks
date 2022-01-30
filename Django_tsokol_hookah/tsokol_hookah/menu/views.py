from django.shortcuts import render
from django.views.generic import ListView, DetailView
from menu.models import Menu


# def menu_list(request):
#     menu = Menu.objects.all()
#     context = {
#         "products": menu
#     }
#     return render(request, 'menu/menu_list.html', context=context)


class MenuListView(ListView):
    model = Menu

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.select_related().prefetch_related()
    #     return qs


class MenuListDetailView(DetailView):
    model = Menu
    fields = "__all__"
