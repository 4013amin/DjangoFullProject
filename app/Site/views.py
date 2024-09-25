from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def home(request):
    banners = models.DataProductBanner.objects.all()[:4]

    context = {'banners': banners}

    return render(request, 'index.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(models.BlogData, id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogTesti.html', context)
