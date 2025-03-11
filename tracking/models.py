from django.db import models

class Bus(models.Model):
    bus_id = models.CharField(max_length=10, unique=True)
    line = models.CharField(max_length=5)  # Line number (1,3,5,sp)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField(default=10)  # Speed in m/s
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Bus {self.bus_id} on Line {self.line}"
