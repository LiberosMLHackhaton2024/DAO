from sqlalchemy import *
from enum import Enum as enumEnum
from typing import Self

from base_database import Base

class AmmoStatus(enumEnum):
	RED = 1
	YELLOW = 2
	GREEN = 3

class Unit(Base):
	__tablename__ = "units"

	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable = False)
	ammo = Column(Enum(AmmoStatus))

	def __init__(self: Self, name: str = None, ammo: AmmoStatus = None):
		self.name = name
		self.ammo = ammo

	def __repr__(self):
		return f"Unit({self.name}, {self.ammo})"