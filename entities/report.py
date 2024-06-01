from sqlalchemy import *
from typing import Self
from sqlalchemy.orm import relationship

from common_base import Base
from entities.ally import Ally

class Report(Base):
	__tablename__ = "reports"

	id = Column(Integer, primary_key = True)

	sent_by = Column(Integer, ForeignKey("allies.id"))
	sender = relationship("Ally", backref = "allies", lazy = False)
	
	recording = Column(Integer)

	type = Column(String(50))

	__mapper_args__ = {
		'polymorphic_on': type,
		'polymorphic_identity': 'report'
	}

	def __init__(self: Self, sender: Ally, recording: int):
		self.sender = sender
		self.recording = recording

	def __repr__(self):
		return f"Report({self.sender}, {self.recording})"
	
	def apply(self: Self):
		...