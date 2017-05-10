# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Product
from django.shortcuts import render

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})
