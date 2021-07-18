from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  *

# Create your views here.

class ChartView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = Sales.objects.all()

        labels = []
        default_items = []

        for item in qs:
            labels.append(item.name)
            default_items.append(item.profit)

        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)