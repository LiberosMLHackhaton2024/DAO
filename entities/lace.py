from sqlalchemy import Column, Integer, ForeignKey, String
from typing import Self, Any

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

	def __init__(self: Self, sender: Ally | None = None, recording: Any | None = None, transcription: str | None = None, liquids: str | None = None, ammunition: str | None = None, casualties: str | None = None, equipment: str | None = None):
		super().__init__(sender, recording, transcription)
		self.liquids = liquids
		self.ammunition = ammunition
		self.casualties = casualties
		self.equipment = equipment

	def __repr__(self: Self):
		return f"LACE({self.sender}, {self.recording}, {self.transcription}, {self.liquids}, {self.ammunition}, {self.casualties}, {self.equipment})"

