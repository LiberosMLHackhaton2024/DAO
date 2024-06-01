from sqlalchemy import *
from typing import Self
from sqlalchemy.orm import relationship

from common_base import Base
from entities.ally import Ally
from entities.report import Report

class SALTR(Report):
	__tablename__ = 'saltr_reports'
	id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
	situation = Column(String(64))
	action = Column(String(64))
	location = Column(String(64))
	time = Column(String(64))
	reaction = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'saltr'
	}

	def __init__(self: Self, sender: Ally = None, recording: int = None, situation: str = None, action: str = None, location: str = None, time: str = None, reaction: str = None):
		super().__init__(recording)
		self.situation = situation
		self.action = action
		self.location = location
		self.time = time
		self.reaction = reaction

	def __repr__(self):
		return f"SALTR({self.sender}, {self.recording}, {self.situation}, {self.action}, {self.location}, {self.time}, {self.reaction})"
