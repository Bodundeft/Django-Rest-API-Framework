from django.shortcuts import render,redirect
from.models import Chef,MainMenu,MenuItems, Drink
from .forms import *
from rest_framework.decorators import api_view
from .serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def index(request):
    form = Contactform
    if request.method == 'POST':
        form = Contactform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('home')

    menus = MainMenu.objects.all()
    data = {
        'menus': menus,
        'form':form,

    }
    return render(request,'pages/index.html',data)

def menuitems(request):
    menuitems = MenuItems.objects.all()
    menus = MainMenu.objects.all()

    data = {
        'menuitems':menuitems,
        'menus':menus
    }
    return render(request,'pages/menulist.html',data)

def menudetails(request,name):
    menuitems = MenuItems.objects.filter(main_menu__name=name)
    menus = MainMenu.objects.all()

    data = {
        'title': MainMenu.objects.get(name=name),
        'menuitems' : menuitems,
        'menus': menus,
    }
    return render(request, 'pages/menudetails.html', data)


@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)