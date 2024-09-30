from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import csv
from .models import *
from .serializers import *
from django.core.cache import cache


class IndexAPIView(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = IndexSerializer


class DeviceAPIView(APIView):
    def get(self, request):
        devices = Device.objects.values()
        cats = Category.objects.all().values()
        print(cats)
        devices_data = []
        for device in devices:
            for cat in cats:
                if cat["id"] == device["cat_id"]:
                    device["category"] = cat["category"]
            photo_url = "http://127.0.0.1:8000/media/" + device["photo"]
            device["photo"] = photo_url
            description = list(Description.objects.filter(device_id=device["id"]).values("description_paragraph"))
            devices_data.append(device | {"description": description})
            device = device | {"description": description}

        return Response({"devices_data": devices_data})


class SelectedCardAPIView(APIView):
    def get(self, request):
        device_id = SelectedCard.objects.all().values("card_id")[0]["card_id"]
        device = Device.objects.filter(id=device_id).values()[0]
        cat = Category.objects.filter(id=device["cat_id"]).values("category")[0]
        print(cat)
        description = list(Description.objects.filter(device_id=device_id).values("description_paragraph"))
        photo_url = "http://127.0.0.1:8000/media/" + device["photo"]
        device["photo"] = photo_url
        device = device | {"description": description} | cat
        return Response(device)

    def post(self, request):
        serializer = SelectedDeviceSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            devices = SelectedCard.objects.all().delete()
            device = SelectedCard.objects.create(card_id=request.data["card_id"])
            device.save()
            return Response("Success!")
        return Response("Data is not valid!")


class AddDescriptionAPIView(APIView):
    def post(self, request):
        Description.objects.create(device=request.data["device"], description_paragraph=request.data["description_paragraph"]).save()


