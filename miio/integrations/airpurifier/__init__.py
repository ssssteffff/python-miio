"""Air purifier integrations."""

from miio.integrations.airdog.airpurifier import AirDogX3
from miio.integrations.dmaker.airfresh import AirFreshA1, AirFreshT2017
from miio.integrations.zhimi.airpurifier import AirFresh, AirPurifier, AirPurifierMiot

__all__ = [
    "AirDogX3",
    "AirFresh",
    "AirFreshA1",
    "AirFreshT2017",
    "AirPurifier",
    "AirPurifierMiot",
]
