from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


def top_page(request):
    return render(request,'menu/top.html',)


def menu_list(request):
    return render(request, 'menu/menu_list.html')



