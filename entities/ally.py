from sqlalchemy import *
from typing import Self

from entities.point import Point

class Ally(Point):
	__tablename__ = "allies"

	id = Column(Integer, ForeignKey('points.id'), primary_key=True)
	name = Column(String(64), nullable = False)

	losses = Column(Integer)
	ammunition = Column(Integer)
	equipment = Column(Integer)

	realized = Column(String(64))
	realizing = Column(String(64))
	will_realize = Column(String(64))
	completed = Column(String(64))
	necessities_other = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'ally'
	}

	def __init__(self: Self, name: str = None, losses: int = None, ammunition: int = None, equipment: int = None, location: str = None, time: int = None, realized: str = None, realizing: str = None, will_realize: str = None, completed: str = None, necessities_other: str = None):
		super().__init__(location, time)

		self.name = name

		self.losses = losses
		self.ammunition = ammunition
		self.equipment = equipment

		self.realized = realized
		self.realizing = realizing
		self.will_realize = will_realize
		self.completed = completed
		self.necessities_other = necessities_other

	def __repr__(self):
		return f"Ally({self.name}, {self.losses}, {self.ammunition}, {self.equipment}, {self.location}, {self.time}, {self.realized}, {self.realizing}, {self.will_realize}, {self.completed}, {self.necessities_other})"
