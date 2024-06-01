from sqlalchemy import *
from typing import Self
from sqlalchemy.orm import relationship

from common_base import Base
from entities.ally import Ally
from entities.report import Report

class LACE(Report):
	__tablename__ = 'lace_reports'
	id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
	liquids = Column(String(64))
	ammunition = Column(String(64))
	casualties = Column(String(64))
	equipment = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'lace'
	}

	def __init__(self: Self, recording: int, liquids: str = None, ammunition: str = None, casualties: str = None, equipment: str = None):
		super().__init__(recording)
		self.liquids = liquids
		self.ammunition = ammunition
		self.casualties = casualties
		self.equipment = equipment

	def __repr__(self: Self):
		return f"LACE({self.recording}, {self.liquids}, {self.ammunition}, {self.casualties}, {self.equipment})"

