from . import views
from django.urls import path, include

urlpatterns = [
    path('category/', views.category_list),
    path('category/<int:pk>/', views.category_details)
]
