from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from dashboard.services import *
import json
from datetime import datetime


def home_page(request):
    if request.GET:

        product = get_product_by_id(request.GET.get("product_id", 0))
        return JsonResponse(product)

    products = []
    categories = Category.objects.all()
    for category in categories:
        products.append(
            {
                "category": category.name,
                "products": Product.objects.filter(category_id=category.id)
            }
        )
    orders = []
    orders_list = request.COOKIES.get("orders")
    if orders_list:
        for key, val in json.loads(orders_list).items():
            orders.append(
                {
                    "product": Product.objects.get(pk=int(key)),
                    "count": val
                }
            )
    ctx = {
        "products": products,
        "categories": categories,
        "orders": orders
    }
    response = render(request, 'new/index.html', ctx)
    return response


def order_save(request):
    if request.POST and int(request.COOKIES.get("total_price", 0)):
        new_order = Order()
        new_order.total_price = request.COOKIES.get("total_price", 0)
        new_order.products = request.COOKIES.get("orders", {})
        new_order.status = 1
        new_order.created_at = datetime.now()
        new_order.save()

        response = redirect("order-page")
        response.set_cookie("total_price", 0)
        response.set_cookie("orders", {})

        return response
    else:
        return redirect("home-page")



def order_page(request):
    return render(request, 'new/order.html')














