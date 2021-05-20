from django.shortcuts import render, HttpResponse
from .models import OnePixel


def Reg(request):
    return render(request, "main/reg.html")


def AllPixelsInfo(request):
    pixelsList = OnePixel.objects.all
    return render(request, "main/index.html", {"all": pixelsList})


def CurrentPixel(request, PrimaryKey):
    Pixel = OnePixel.objects.get(id=PrimaryKey)
    Color = Pixel.PixelColor
    PixelName = Pixel.name_of_PC
    return render(request, "main/pixel.html", {"PixelName": PixelName, "PixelColor": Color})
