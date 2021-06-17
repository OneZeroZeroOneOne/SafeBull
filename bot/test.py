import datetime
import os
from enum import Enum


class Lang(Enum):
    ru = 1
    en = 2

print(Lang['ru'].name)