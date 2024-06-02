from sqlalchemy import Column, Integer, ForeignKey, String
from typing import Self, Any
from sqlalchemy.orm import Session

from entities.report import Report
from entities.ally import Ally

class SAS(Report):
	__tablename__ = 'sas_reports'
	id = Column(Integer, ForeignKey('reports.id'), primary_key = True)

	losses = Column(Integer)
	ammunition = Column(Integer)
	equipment = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'sas'
	}

	def __init__(self: Self, sender: Ally | None = None, recording: Any | None = None, transcription: str | None = None, losses: int | None = None, ammunition: int | None = None, equipment: int | None = None):
		super().__init__(sender, recording, transcription)
		self.losses = losses
		self.ammunition = ammunition
		self.equipment = equipment

	def __repr__(self: Self):
		return f"SAS({self.sender}, {self.recording}, {self.transcription}, {self.size}, {self.activity}, {self.location}, {self.uniforms}, {self.time}, {self.equipment})"
	
	def apply(self: Self, session: Session):
		# Access the sender associated with this report
		sender = self.sender
		
		# Increase the sender's losses by the losses reported in this SAS report
		if sender is not None and sender.losses is not None and self.losses is not None:
			sender.losses += self.losses
		
		# Update the sender's ammunition and equipment status based on this SAS report
		sender.ammunition = self.ammunition
		sender.equipment = self.equipment
		
		# Commit the changes to the database
		# from sqlalchemy.orm import Session
		# session = Session()
		session.merge(sender)  # Use merge to handle existing entries
		session.commit()
