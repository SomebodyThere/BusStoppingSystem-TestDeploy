from django.db import models
from django.utils import timezone

import datetime

class BusModel(models.Model) :
    model_name = models.CharField(max_length=200)
    model_serial_number = models.CharField(max_length=200)
    max_passenger = models.IntegerField()
    engine = models.CharField(max_length=200)
    low_floow_TF = models.BooleanField()
    def __str__(self):
        return self.model_name

class Route(models.Model) :
    route_name = models.CharField(max_length=10)
    def __str__(self):
        return self.route_name

class BusStation(models.Model) :
    station_name = models.CharField(max_length=200)
    stop_time = models.IntegerField()
    latitude = models.FloatField(blank=True, null=False)
    longitude = models.FloatField(blank=True, null=False)

    def __str__(self):
        return self.station_name
    # 코드 추가. 확인 바람
    def get_route(self):
        route = []
        data = self.station_route.all()
        for i in data:
            route.append(i.route.route_name)
        return route

class Bus(models.Model) :
    bus_model = models.ForeignKey(BusModel, on_delete=models.CASCADE)
    bus_license_number = models.CharField(max_length=20)
    bus_status = models.CharField(max_length=10)
    def __str__(self):
        return self.bus_license_number
    
class Dispatch(models.Model) :
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    start_time = models.TimeField()
    
    class Meta:
        ordering = ['route', 'bus']
    def __str__(self) :
        return "{}번 노선 {} 차량".format(str(self.route), str(self.bus))

class Reserve(models.Model) :
    bus_station = models.ForeignKey(BusStation, on_delete=models.CASCADE)
    dispatch= models.ForeignKey(Dispatch, on_delete=models.CASCADE)
    reserve_count = models.IntegerField()

class StationRoute(models.Model) :
    bus_station = models.ForeignKey(BusStation, on_delete=models.SET_NULL, null=True, related_name='station_route')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='route_station')
    order_num = models.IntegerField()
    move_time = models.IntegerField(null=True)

    class Meta:
        ordering = ['route', 'order_num']

    def __str__(self):
        return "{}번 노선 {} 번째 {} 정류장".format(str(self.route), str(self.order_num), str(self.bus_station))