from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from charts.models import Chartdata
from charts.serializer import ChartSerailizer
from django.http.response import JsonResponse
from rest_framework import viewsets

"""def chartApi(request):
    if request.method == 'GET':
        charts = Chartdata.objects.all()
        charts_serializer = ChartSerailizer(charts,many = True)
        return JsonResponse(charts_serializer.data,safe=False)
    
    elif request.method == 'POST':
        chart_data = JSONParser().parse(request)
        chart_serializer = ChartSerailizer(data=chart_data)
        if chart_serializer.is_valid():
            chart_serializer.save()
            return JsonResponse("Added Sucessfully !!", safe=False)
        return JsonResponse("Post Failed",safe=False)

# Create your views here."""

class ChartViewSet(viewsets.ModelViewSet):
    serializer_class=ChartSerailizer
    queryset=Chartdata.objects.all()
