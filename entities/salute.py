from sqlalchemy import *
from typing import Self
from sqlalchemy.orm import relationship

from entities.report import Report

class SALUTE(Report):
	__tablename__ = 'salute_reports'
	id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
	size = Column(String(64))
	activity = Column(String(64))
	location = Column(String(64))
	uniforms = Column(String(64))
	time = Column(String(64))
	equipment = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'salute'
	}

	def __init__(self: Self, recording: int, size: str = None, activity: str = None, location: str = None, uniforms: str = None, time: str = None, equipment: str = None):
		super().__init__(recording)
		self.size = size
		self.activity = activity
		self.location = location
		self.uniforms = uniforms
		self.time = time
		self.equipment = equipment

	def __repr__(self):
		return f"SALUTE({self.recording}, {self.size}, {self.activity}, {self.location}, {self.uniforms}, {self.time}, {self.equipment})"