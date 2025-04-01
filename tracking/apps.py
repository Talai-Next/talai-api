from django.apps import AppConfig
import logging
import os
import sys

logger = logging.getLogger(__name__)


class TrackingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracking"

    def ready(self):
        if os.environ.get("RUN_MAIN") != "true":
            return

        if "runserver" in sys.argv:
            logger.info("Starting bus simulation thread...")
            from tracking.bus_simulation import start_simulation
            start_simulation()
