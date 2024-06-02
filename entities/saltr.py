from sqlalchemy import Column, Integer, ForeignKey, String
from typing import Self, Any

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

	def __init__(self: Self, sender: Ally | None = None, recording: Any | None = None, transcription: str | None = None, situation: str | None = None, action: str | None = None, location: str | None = None, time: str | None = None, reaction: str | None = None):
		super().__init__(sender, recording, transcription)
		self.situation = situation
		self.action = action
		self.location = location
		self.time = time
		self.reaction = reaction

	def __repr__(self: Self):
		return f"SALTR({self.sender}, {self.recording}, {self.transcription}, {self.situation}, {self.action}, {self.location}, {self.time}, {self.reaction})"
