from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


def gacha(request):
    return render(request, 'gacha/gacha.html')