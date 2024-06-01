from sqlalchemy import *
# from enum import Enum as enumEnum
from typing import Self

from common_base import Base

# class ColorStatus(enumEnum):
# 	RED = 1
# 	YELLOW = 2
# 	GREEN = 3

class Ally(Base):
	__tablename__ = "allies"

	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable = False)

	losses = Column(Integer)
	ammunition = Column(Integer)
	equipment = Column(Integer)

	location = Column(String(64), nullable = False)
	realized = Column(String(64), nullable = False)
	realizing = Column(String(64), nullable = False)
	will_realize = Column(String(64), nullable = False)
	completed = Column(String(64), nullable = False)
	necessities_other = Column(String(64), nullable = False)

	def __init__(self: Self, name: str = None, losses: int = None, ammunition: int = None, equipment: int = None, location: str = None, realized: str = None, realizing: str = None, will_realize: str = None, completed: str = None, necessities_other: str = None):
		self.name = name

		self.losses = losses
		self.ammunition = ammunition
		self.equipment = equipment

		self.location = location
		self.realized = realized
		self.realizing = realizing
		self.will_realize = will_realize
		self.completed = completed
		self.necessities_other = necessities_other

	def __repr__(self):
		return f"Ally({self.name}, {self.ammo})"