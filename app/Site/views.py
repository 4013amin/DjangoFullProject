from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def home(request):
    banners = models.DataProductBanner.objects.all()[:4]

    topten = models.ProductTop.objects.all()

    context = {'banners': banners, 'topten': topten}

    return render(request, 'index.html', context)
