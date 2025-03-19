from django.http import JsonResponse
from .models import Client, Order, Driver
from .serializers import ClientSerializer, DriverSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        return render(request, "main/index.html")

@api_view(['GET', 'POST'])
def sign_in(request):

    if request.method == 'GET':
        return render(request, "main/signin.html")

    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def sign_up(request):

    if request.method == 'GET':
        return render(request, "main/signup.html")

    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def client_list(request):

    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return render(request, "main/clients.html", {'clients': clients})

    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def driver_list(request):
    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return render(request, "main/drivers.html", {'drivers': drivers})

    if request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET', 'POST'])
def make_order(request):
    if request.method == 'GET':
        return render(request, "main/make_order.html")

@api_view(['GET', 'POST'])
def order_list(request):
    clients = Client.objects.all()  # Fetch all clients
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return render(request, "main/orders.html", {'orders': serializer.data, 'clients': clients})

    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, id):
    try:
        client = Client.objects.get(pk=id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return render(request, 'main/client_detail.html', {'client': serializer.data})

    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'main/client_detail.html', {'client': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, id):
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return render(request, 'main/make_order.html', {'order': serializer.data})
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, id):
    try:
        driver = Driver.objects.get(pk=id)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DriverSerializer(driver)
        return render(request, 'main/driver_detail.html', {'driver': serializer.data})
    elif request.method == 'PUT':
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

