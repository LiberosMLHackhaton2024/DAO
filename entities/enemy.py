from sqlalchemy import Column, Integer, ForeignKey, String
from typing import Self

from entities.point import Point

class Enemy(Point):
	__tablename__ = "enemies"

	id = Column(Integer, ForeignKey('points.id'), primary_key=True)

	size = Column(Integer)
	activity = Column(String(64))
	# location = Column(String(64))
	uniforms = Column(String(64))
	# time = Column(Integer)
	equipment = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'enemy'
	}

	def __init__(self: Self, size: int | None = None, activity: str | None = None, location_x: float | None = None, location_y: float | None = None, uniforms: str | None = None, time: int | None = None, equipment: str | None = None):
		super().__init__(location_x, location_y, time)
		self.size = size
		self.activity = activity
		# self.location = location
		self.uniforms = uniforms
		self.equipment = equipment

	def __repr__(self):
		return f"Enemy({self.size}, {self.activity}, {self.location}, {self.uniform}, {self.time}, {self.equipment})"
