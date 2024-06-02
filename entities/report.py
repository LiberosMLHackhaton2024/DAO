from sqlalchemy import Column, Integer, ForeignKey, String
from typing import Self, Any
from sqlalchemy.orm import relationship

from common_base import Base
from entities.ally import Ally

class Report(Base):
	__tablename__ = "reports"

	id = Column(Integer, primary_key = True)

	sent_by = Column(Integer, ForeignKey("allies.id"))
	sender = relationship("Ally", backref = "allies", lazy = False)
	
	recording = Column(String(64))
	transcription = Column(String(64))

	type = Column(String(50))

	__mapper_args__ = {
		'polymorphic_on': type,
		'polymorphic_identity': 'report'
	}

	def __init__(self: Self, sender: Ally | None = None, recording: Any | None = None, transcription: str | None = None) -> None:
		self.sender = sender
		self.recording = recording
		self.transcription = transcription

	def __repr__(self: Self) -> str:
		return f"Report({self.sender}, {self.recording}, {self.transcription})"
	
	def apply(self: Self):
		...