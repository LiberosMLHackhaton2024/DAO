from sqlalchemy import Column, Integer, ForeignKey, String
from typing import Self
from sqlalchemy.orm import relationship

from common_base import Base
from entities.ally import Ally
from entities.report import Report

class SLLS(Report):
	__tablename__ = 'slls_reports'
	id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
	stop = Column(String(64))
	listen = Column(String(64))
	look = Column(String(64))
	smell = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'slls'
	}

	def __init__(self: Self, sender: Ally | None = None, recording: int | None = None, stop: str | None = None, listen: str | None = None, look: str | None = None, smell: str | None = None):
		super().__init__(sender, recording)
		self.stop = stop
		self.listen = listen
		self.look = look
		self.smell = smell

	def __repr__(self):
		return f"SLLS({self.sender}, {self.recording}, {self.stop}, {self.listen}, {self.look}, {self.smell})"
