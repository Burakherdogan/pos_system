from django.shortcuts import render, get_object_or_404
from .models import Products
from .cart import Cart
from django.http import JsonResponse


def index(request):
    products = {
        "products": Products.objects.all(),
    }
    return render(request, "main/index.html",products)

def reports(request):
    return render(request, "main/reports.html")

def shopping_cart(request):
    return render(request, "shopping_cart.html",{})

def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test post
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        # lookup product in DB
        product = get_object_or_404(Products, id=product_id)
        # save to session
        cart.add(product=product)
        #get cart quantity
        cart_quantity = cart.__len__()
        # return response
        response = JsonResponse({'qty': cart_quantity})
        return response
    
def cart_delete(request):
    pass

def cart_update(request):
    pass