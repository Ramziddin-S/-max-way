from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from way.models import *
from . import services


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    categories = services.get_categories_news_count()

    ctx = {
        'categories': categories
    }
    return render(request, 'dashboard/index.html', ctx)

@login_required_decorator
def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')




@login_required_decorator
def category_list(request):
    categories = services.get_categories()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)

@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html',ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=model)
    print(model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/category/form.html', ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(id=pk)
    model.delete()
    return redirect('category_list')

@login_required_decorator
def product_list(request):
    products = services.get_product()
    ctx = {
        "products": products
    }
    print(products)
    return render(request, 'dashboard/product/list.html', ctx)

@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
    'form': form
                 }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(id=pk)
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
                 }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(id=pk)
    model.delete()
    return redirect("product_list")


@login_required_decorator
def user_list(request):
    users = services.get_user()
    ctx = {
        "users": users
    }
    return render(request, 'dashboard/user/list.html', ctx)


@login_required_decorator
def user_create(request):
    user = User()
    form = UserForm(request.POST, request.FILES,instance=user)
    if request.POST:
        print(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('user_list')
    else:
        print(form.errors)
    ctx = {
        "form": form,
        "user": user
                 }
    return render(request, 'dashboard/user/form.html', ctx)


@login_required_decorator
def user_edit(request, pk):
    model = User.objects.get(id=pk)
    form = UserForm(request.POST or None, instance=model)
    if request.POST:
        print(99)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/user/form.html', ctx)


@login_required_decorator
def user_delete(request, pk):
    model = User.objects.get(id=pk)
    model.delete()
    return redirect('user_list')



@login_required_decorator
def order_list(request):
    orders = services.get_status_info([1, 2, 3])
    if request.POST:
        filter = request.POST.get("order_filter")

        if filter == "done":
            orders = services.get_status_info([2])

        elif filter == "failed":
            orders = services.get_status_info([3])


    ctx = {
        "orders": orders
    }
    return render(request, 'dashboard/order/list.html', ctx)



@login_required_decorator
def order_create(request, pk):
    model = Order.objects.get(id=pk)
    form = OrderForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('order_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
                 }
    return render(request, 'dashboard/order/form.html', ctx)


@login_required_decorator
def order_status(request, pk, status):
    model = Order.objects.get(id=pk)
    model.status = status
    model.save()
    return redirect("order_list")


@login_required_decorator
def order_edit(request, pk):
    model = Order.objects.get(id=pk)
    form = OrderForm(request.POST or None, instance=model)
    if request.POST:
        print(99)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/order/form.html', ctx)


@login_required_decorator
def order_delete(request, pk):
    model = Order.objects.get(id=pk)
    model.delete()
    return redirect('order_list')
