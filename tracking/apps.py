from django.apps import AppConfig
import threading
from django.db.models.signals import post_migrate
import logging
logger = logging.getLogger(__name__)


class TrackingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracking"

    def ready(self):
        logger.info(f"threading...")
        from tracking.bus_simulation import start_simulation

        start_simulation()
