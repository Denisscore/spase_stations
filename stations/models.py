import uuid
from django.utils.translation import gettext_lazy as translate
from django.contrib.gis.db import models
from users.models import User


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(translate("created"), auto_now_add=True)
    breaking = models.DateTimeField(translate("breaking"))

    class Meta:
        abstract = True

class Station(UUIDMixin, TimeStampedMixin):

    class ConditionChoices(models.TextChoices):
        RUNNING = "running", translate("running")
        BROKEN = 'broken', translate("broken")

    name = models.CharField(translate('name'), max_length=255)
    description = models.TextField(translate("description"), blank=True)
    condition = models.CharField(
        translate("condition"),
        default=ConditionChoices.RUNNING,
        choices=ConditionChoices.choices,
        max_length=7
    )

class Indication(UUIDMixin):
    user = models.ForeignKey(User, verbose_name=translate("command initiator"), on_delete=models.CASCADE)
    axis = models.PointField(default=100, null=True, verbose_name=translate("coordinate"), blank=True)
    distans = models.IntegerField(verbose_name=translate("distans"))


