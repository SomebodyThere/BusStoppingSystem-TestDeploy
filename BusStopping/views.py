from django.shortcuts import render
from rest_framework import viewsets
from BusStopping.models import BusModel, Route, BusStation, Bus, Dispatch, Reserve, StationRoute
from BusStopping.serializers import BusModelSerializer, RouteSerializer, BusStationSerializer, BusSerializer, DispatchSerializer, ReserveSerializer, StationRouteSerializer

class BusModelViewset(viewsets.ModelViewSet) :
    queryset = BusModel.objects.all()
    serializer_class = BusModelSerializer

class RouteViewset(viewsets.ModelViewSet) :
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class BusStationViewset(viewsets.ModelViewSet) :
    queryset = BusStation.objects.all()
    serializer_class = BusStationSerializer

class BusViewset(viewsets.ModelViewSet) :
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class DispatchViewset(viewsets.ModelViewSet) :
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

class ReserveViewset(viewsets.ModelViewSet) :
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer

class StationRouteViewset(viewsets.ModelViewSet) :
    queryset = StationRoute.objects.all()
    serializer_class = StationRouteSerializer
