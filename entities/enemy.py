from sqlalchemy import *
from enum import Enum as enumEnum
from typing import Self

from common_base import Base

class Enemy(Base):
	__tablename__ = "units"

	id = Column(Integer, primary_key = True)

	size = Column(Integer)
	activity = Column(String(64))
	location = Column(String(64))
	uniform = Column(String(64))
	time = Column(Integer)
	equipment = Column(String(64))

	def __init__(self: Self, size: int = None, activity: str = None, location: str = None, uniform: str = None, time: int = None, equipment: str = None):
		self.size = size
		self.activity = activity
		self.location = location
		self.uniform = uniform
		self.time = time
		self.equipment = equipment

	def __repr__(self):
		return f"Unit({self.name}, {self.ammo})"