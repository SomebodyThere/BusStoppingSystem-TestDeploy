from rest_framework import serializers
from BusStopping.models import BusModel, BusStation, Dispatch, Bus, Reserve, Route, StationRoute

class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'
class BusModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusModel
        fields = '__all__'
class BusStationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusStation
        fields = ['url', 'station_name', 'stop_time', 'latitude', 'longitude', 'get_route']
class DispatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dispatch
        fields = '__all__'
class ReserveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'
class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
class StationRouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StationRoute
        fields = '__all__'