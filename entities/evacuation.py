from sqlalchemy import *
from enum import Enum as enumEnum
from typing import Self

from entities.point import Point

class Evacuation(Point):
	__tablename__ = "units"

	id = Column(Integer, ForeignKey('points.id'), primary_key=True)

	size = Column(Integer)			# number of people in need of evacuation
	frequency = Column(Float)
	activity = Column(String(64))
	equipment = Column(String(64))	# required
	safety = Column(String(64))
	landing_site_marking = Column(String(64))
	nationality = Column(String(64))
	contamination = Column(String(64))
	# uniforms = Column(String(64))
	# time = Column(Integer)
	

	__mapper_args__ = {
		'polymorphic_identity': 'evacuation'
	}

	def __init__(self: Self, size: int = None, frequency: float = None, activity: str = None, equipment: str = None, safety: str = None, landing_site_marking: str = None, nationality: str = None, contamination: str = None):
		super().__init__()
		self.size = size
		self.frequency = frequency
		self.activity = activity
		self.equipment = equipment
		self.safety = safety
		self.landing_site_marking = landing_site_marking
		self.nationality = nationality
		self.contamination = contamination

	def __repr__(self):
		return f"Evacuation({self.size}, {self.frequency}, {self.activity}, {self.equipment}, {self.safety}, {self.landing_site_marking}, {self.nationality}, {self.contamination})"
