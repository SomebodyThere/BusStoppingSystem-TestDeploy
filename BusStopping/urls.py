from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BusStopping import views

router = DefaultRouter()
router.register(r'BusModel', views.BusModelViewset)
router.register(r'Route', views.RouteViewset)
router.register(r'BusStation', views.BusStationViewset)
router.register(r'Bus', views.BusViewset)
router.register(r'Dispatch', views.DispatchViewset)
router.register(r'Reserve', views.ReserveViewset)
router.register(r'StationRoute', views.StationRouteViewset)

urlpatterns = [
    path("", include(router.urls)),
]