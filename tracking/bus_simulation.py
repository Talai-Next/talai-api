import time
import random
import geopy.distance
import threading
from django.db import transaction
from django.conf import settings
from .models import Bus

ROUTE_DATA = settings.ROUTE_DATA

def start_simulation():
    """Start simulations for all active buses across all lines."""
    print("Starting bus simulation...")
    try:
        buses = Bus.objects.filter(active=True)
        if not buses.exists():
            print("No active buses found. Simulation will not start.")
            return

        threads = []

        for bus in buses:
            simulator = BusSimulator(bus)
            thread = threading.Thread(target=simulator.move_bus, daemon=True)
            thread.start()
            threads.append(thread)

        print(f"{len(threads)} bus(es) started simulation.")

    except Exception as e:
        print(f"Error in simulation: {e}")

class BusSimulator:
    def __init__(self, bus):
        self.bus = bus
        self.route = ROUTE_DATA.get(bus.line)
        self.current_index = 0
        self.running = True

    def adjust_speed(self):
        base_speed = 10  # Default speed (m/s)
        node_name = self.route.iloc[self.current_index]["Node_Name"].lower()
        instruction = self.route.iloc[self.current_index]["Instruction"].lower()

        if "stop" in node_name and random.random() < 0.25:
            if random.random() < 0.5:
                self.bus.speed = 0
            else:
                self.bus.speed = base_speed
        elif "zebra" in node_name and random.random() < 0.25:
            self.bus.speed = base_speed / 2
        elif "speed bump" in node_name:
            self.bus.speed = base_speed / 3
        elif "turn" in instruction:
            self.bus.speed = base_speed / 2
        else:
            self.bus.speed = base_speed

    def move_bus(self):
        """Moves the bus along its designated route."""
        while self.running and self.current_index < len(self.route) - 1:
            next_index = self.current_index + 1
            next_lat = self.route.iloc[next_index]["Latitude"]
            next_lon = self.route.iloc[next_index]["Longitude"]
            distance = geopy.distance.geodesic(
                (self.bus.latitude, self.bus.longitude), (next_lat, next_lon)
            ).meters

            self.adjust_speed()

            if self.bus.speed == 0:
                print(f"Bus {self.bus.bus_id} stopping at {self.route.iloc[next_index]['Node_Name']}...")
                time.sleep(random.randint(2, 5))
            else:
                num_steps = max(1, int(distance / self.bus.speed))
                lat_step = (next_lat - self.bus.latitude) / num_steps
                lon_step = (next_lon - self.bus.longitude) / num_steps

                for _ in range(num_steps):
                    if not self.running:
                        break
                    self.bus.latitude += lat_step
                    self.bus.longitude += lon_step

                    with transaction.atomic():
                        self.bus.save()

                    print(f"Bus {self.bus.bus_id} - LAT: {self.bus.latitude:.5f}, LON: {self.bus.longitude:.5f}, SPEED: {self.bus.speed:.2f} m/s")
                    time.sleep(1)

                self.current_index = next_index

    def stop_bus(self):
        """Stops the bus simulation."""
        self.running = False
