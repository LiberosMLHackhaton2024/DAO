from sqlalchemy import *
from enum import Enum as enumEnum
from typing import Self

from mappoints.base_mappoints import Base

class ColorStatus(enumEnum):
	RED = 1
	YELLOW = 2
	GREEN = 3

class Unit(Base):
	__tablename__ = "units"

	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable = False)
	ammo = Column(Enum(ColorStatus))

	def __init__(self: Self, name: str = None, ammo: ColorStatus = None):
		self.name = name
		self.ammo = ammo

	def __repr__(self):
		return f"Unit({self.name}, {self.ammo})"