from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PriceInputForm


def gacha(request):
    if request.method == 'POST':
        form = PriceInputForm(request.POST)
        if form.is_valid():
            form.save()
            
        return render(request, 'gacha/gacha.html', {"form": form})
    else:
        form = PriceInputForm()
        return render(request, 'gacha/gacha.html', {"form": form})

