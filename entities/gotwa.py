from sqlalchemy import Column, Integer, ForeignKey, String
from typing import Self
from sqlalchemy.orm import relationship

from common_base import Base
from entities.ally import Ally
from entities.report import Report

class GOTWA(Report):
	__tablename__ = 'gotwa_reports'
	id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
	going = Column(String(64))
	others = Column(String(64))
	time = Column(Integer)
	what = Column(String(64))
	action = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'gotwa'
	}

	def __init__(self: Self, sender: Ally | None = None, recording: int | None = None, going: str | None = None, others: str | None = None, time: str | None = None, what: str | None = None, action: str | None = None):
		super().__init__(sender, recording)
		self.going = going
		self.others = others
		self.time = time
		self.what = what
		self.action = action

	def __repr__(self: Self):
		return f"GOTWA({self.sender}, {self.recording}, {self.going}, {self.others}, {self.time}, {self.what}, {self.action})"

