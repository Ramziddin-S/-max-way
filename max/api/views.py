from way import models
from .serializers import CategorySerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from . import servise
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def category_list(repuest):
    if repuest.method == "GET":
        ctegory = servise.get_category()
        return Response(ctegory, status=status.HTTP_200_OK)

    elif repuest.POST == "POST":
        serializer = CategorySerializer(data=repuest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT"])
def category_details(request, pk):
    if request.method == "GET":
        try:
            category = models.Category.objects.get(id=pk)
        except:
            raise NotFound(f"Categary with pk = {pk} not found!")
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        try:
            category = models.Category.objects.get(id=pk)
        except:
            raise NotFound(f"Category with pk = {pk} not found!")
        serializer = CategorySerializer(data=request.data, instance=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
