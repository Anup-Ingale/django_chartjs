from django.shortcuts import render
from .models import  *


def chartview(request):
    query = Sales.objects.all()
    labels = []
    default_items = []

    for item in query:
        labels.append(item.name_of_sales)
        default_items.append(item.profit)

    data = {
        "labels": labels,
        "datasets": default_items,
    }
    return render(request,'visual.html', {'context': data})
