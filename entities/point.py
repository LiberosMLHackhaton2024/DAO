from sqlalchemy import Column, Integer, String
from typing import Self

from common_base import Base

class Point(Base):
	__tablename__ = "points"

	id = Column(Integer, primary_key = True)

	location = Column(String(64))
	time = Column(Integer)	# time of last contact/report
	type = Column(String(50))

	__mapper_args__ = {
		'polymorphic_on': type,
		'polymorphic_identity': 'point'
	}

	def __init__(self: Self, location: str | None = None, time: int | None = None):
		self.location = location
		self.time = time

	def __repr__(self):
		return f"Point({self.location}, {self.time})"