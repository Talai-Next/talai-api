from django.urls import path
from .views import all_buses, buses_by_line, bus_by_id

urlpatterns = [
    path("buses/", all_buses, name="all_buses"),
    path("buses/line/<str:line>/", buses_by_line, name="buses_by_line"),
    path("buses/<str:bus_id>/", bus_by_id, name="bus_by_id"),
]
