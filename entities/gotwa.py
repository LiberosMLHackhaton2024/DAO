from sqlalchemy import *
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
	time = Column(String(64))
	what = Column(String(64))
	action = Column(String(64))

	__mapper_args__ = {
		'polymorphic_identity': 'gotwa'
	}

	def __init__(self: Self, recording: int, going: str = None, others: str = None, time: str = None, what: str = None, action: str = None):
		super().__init__(recording)
		self.going = going
		self.others = others
		self.time = time
		self.what = what
		self.action = action

	def __repr__(self):
		return f"GOTWA({self.recording}, {self.going}, {self.others}, {self.time}, {self.what}, {self.action})"

