from sqlalchemy import *
from enum import Enum as enumEnum
from typing import Self

from entities.point import Point

class Enemy(Point):
	__tablename__ = "units"

	id = Column(Integer, ForeignKey('points.id'), primary_key=True)

	size = Column(Integer)
	activity = Column(String(64))
	# location = Column(String(64))
	uniform = Column(String(64))
	time = Column(Integer)
	equipment = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'enemy'
	}

	def __init__(self: Self, size: int = None, activity: str = None, location: str = None, uniform: str = None, time: int = None, equipment: str = None):
		super().__init__(location, time)
		self.size = size
		self.activity = activity
		self.location = location
		self.uniform = uniform
		self.equipment = equipment

	def __repr__(self):
		return f"Enemy({self.size}, {self.activity}, {self.location}, {self.uniform}, {self.time}, {self.equipment})"
