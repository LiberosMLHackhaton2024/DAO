from sqlalchemy import Column, Integer, String, Float, Tuple
from typing import Self

from common_base import Base

class Point(Base):
	__tablename__ = "points"

	id = Column(Integer, primary_key = True)

	location_x = Column(Float)
	location_y = Column(Float)
	time = Column(Integer)	# time of last contact/report
	type = Column(String(50))

	__mapper_args__ = {
		'polymorphic_on': type,
		'polymorphic_identity': 'point'
	}

	def __init__(self: Self, location_x: Float | None = None, location_y: Float | None = None, time: int | None = None):
		self.location_x = location_x
		self.location_y = location_y
		self.time = time

	def __repr__(self: Self):
		return f"Point({self.location}, {self.time})"