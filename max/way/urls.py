from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('dashboard/', include('dashboard.urls')),
    path('order/save/', views.order_save, name="order-save"),
    path('order/', views.order_page, name="order-page")


]
