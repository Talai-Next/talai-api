from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Bus
from .serializers import BusSerializer
import logging

@api_view(["GET"])
def all_buses(request):
    """Return all buses."""
    buses = Bus.objects.filter(active=True)
    serializer = BusSerializer(buses, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def buses_by_line(request, line):
    """Return all buses for a specific line."""
    buses = Bus.objects.filter(line=line, active=True)
    serializer = BusSerializer(buses, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def bus_by_id(request, bus_id):
    """Return a specific bus by ID."""
    try:
        bus = Bus.objects.get(bus_id=bus_id, active=True)
        serializer = BusSerializer(bus)
        return Response(serializer.data)
    except Bus.DoesNotExist:
        return Response({"error": "Bus not found"}, status=404)
