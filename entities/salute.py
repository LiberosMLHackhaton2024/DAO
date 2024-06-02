from sqlalchemy import Column, Integer, ForeignKey, String, Float
from typing import Self, Any
from sqlalchemy.orm import Session

from entities.report import Report
from entities.enemy import Enemy
from entities.ally import Ally

class SALUTE(Report):
	__tablename__ = 'salute_reports'
	id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
	size = Column(String(64))
	activity = Column(String(64))
	location_x = Column(Float)
	location_y = Column(Float)
	uniforms = Column(String(64))
	time = Column(String(64))
	equipment = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'salute'
	}

	def __init__(self: Self, sender: Ally | None = None, recording: Any | None = None, transcription: str | None = None, size: int | None = None, activity: str | None = None, location_x: float | None = None, location_y: float | None = None, uniforms: str | None = None, time: int | None = None, equipment: str | None = None):
		super().__init__(sender, recording, transcription)
		self.size = size
		self.activity = activity
		self.location_x = location_x
		self.location_y = location_y
		self.uniforms = uniforms
		self.time = time
		self.equipment = equipment

	def __repr__(self):
		return f"SALUTE({self.recording}, {self.transcription}, {self.size}, {self.activity}, {self.location_x}, {self.location_y}, {self.uniforms}, {self.time}, {self.equipment})"
	
	def apply(self: Self, session: Session):
		# Create a new Enemy instance using attributes from this SALUTE report
		new_enemy = Enemy(
			size=self.size,
			activity=self.activity,
			location_x=self.location_x,
			location_y=self.location_y,
			uniforms=self.uniforms,
			equipment=self.equipment
		)
		
		# Add the new Enemy to the session
		session.add(new_enemy)
		
		# Commit the changes to the database
		session.commit()
