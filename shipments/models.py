from django.contrib.auth import get_user_model
from django.db import models

from django.core.exceptions import FieldDoesNotExist
from django.db.models.deletion import RESTRICT


class Shipments(models.Model):
    shipment_id = models.CharField(unique=True, max_length=100)
    shpment_reference = models.CharField(unique=True, max_length=100)
    user = models.OneToOneField(get_user_model(), on_delete=RESTRICT)
