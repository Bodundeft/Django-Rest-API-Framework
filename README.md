# Django-Rest-API-Framework
---
 Webstack - Portfolio Project
---

*A REST API is a popular way for systems to expose useful functions and data. REST, which stands for representational state transfer, can be made up of one or more resources that can be accessed at a given URL and returned in various formats, like JSON, images, HTML, and more.*


---
## To create a Django REST API for a restaurant, you can follow these steps:
---

*Install Django REST framework using pip1.*

*Create a new Django project and app2.*

*Define your models in the app’s models.py file2.*

*Create serializers for your models in the app’s serializers.py file2.*

*Define views for your API in the app’s views.py file2.*

*Define URLs for your API in the project’s urls.py file2.*

### Here is an example of a Django REST API for a restaurant that includes code 3:

from django.urls import path from .views import MenuItemsView urlpatterns = [ path('menu/', MenuItemsView.as_view(), name='menu-items'), ]

from rest_framework.views import APIView from rest_framework.response import Response from rest_framework import status from .models import MenuItem from .serializers import MenuItemSerializer class MenuItemsView(APIView): def get(self, request): menu_items = MenuItem.objects.all() serializer = MenuItemSerializer(menu_items, many=True) return Response(serializer.data) def post(self, request): serializer = MenuItemSerializer(data=request.data) if serializer.is_valid(): serializer.save() return Response(serializer.data, status=status.HTTP_201_CREATED) return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


---
### To create a Django REST API for a restaurant, you can follow these steps: 
---

-  Install Django REST framework using pip. 
-  Create a new Django project and app. 
-  Define your models in the app's models.py file. 
-  Create serializers for your models in the app's serializers.py file. 
-  Define views for your API in the app's views.py file. 
-  Define URLs for your API in the project's urls.py file. 
-  Here is an example of a Django REST API for a restaurant that includes code: 
python from django.urls import path from .views import MenuItemsView urlpatterns = [ path('menu/', MenuItemsView.as_view(), name='menu-items'), ]  python from rest_framework.views import APIView from rest_framework.response import Response from rest_framework import status from .models import MenuItem from .serializers import MenuItemSerializer class MenuItemsView(APIView): def get(self, request): menu_items = MenuItem.objects.all() serializer = MenuItemSerializer(menu_items, many=True) return Response(serializer.data) def post(self, request): serializer = MenuItemSerializer(data=request.data) if serializer.is_valid(): serializer.save() return Response(serializer.data, status=status.HTTP_201_CREATED) return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


