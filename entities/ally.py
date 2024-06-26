from sqlalchemy import Column, Integer, ForeignKey, String
from typing import Self

from entities.point import Point

class Ally(Point):
	__tablename__ = "allies"

	id = Column(Integer, ForeignKey('points.id'), primary_key=True)
	name = Column(String(64))

	losses = Column(Integer)
	ammunition = Column(Integer)
	equipment = Column(Integer)

	# realized = Column(String(64))
	# realizing = Column(String(64))
	# will_realize = Column(String(64))
	# completed = Column(String(64))
	# necessities_other = Column(String(64))

	situation = Column(String(64))
	action = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'ally'
	}

	def __init__(self: Self, name: str | None = None, losses: int | None = None, ammunition: int | None = None, equipment: int | None = None, location_x: float | None = None, location_y: float | None = None, time: int | None = None, enemy_contact_time: int | None = None, situation: str | None = None, action: str | None = None):
		super().__init__(location_x, location_y, time)

		self.name = name

		self.losses = losses
		self.ammunition = ammunition
		self.equipment = equipment

		# self.realized = realized
		# self.realizing = realizing
		# self.will_realize = will_realize
		# self.completed = completed
		# self.necessities_other = necessities_other
		self.enemy_contact_time = enemy_contact_time
		self.situation = situation
		self.action = action

	def __repr__(self):
		return f"Ally({self.name}, {self.losses}, {self.ammunition}, {self.equipment}, {self.location}, {self.time},  {self.enemy_contact_time})"
