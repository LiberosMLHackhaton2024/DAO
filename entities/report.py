from sqlalchemy import *
from enum import Enum as enumEnum
from typing import Self

from common import Base

# class AmmoStatus(enumEnum):
# 	RED = 1
# 	YELLOW = 2
# 	GREEN = 3

class ReportCategory(enumEnum):
	SALUTE = 1
	SALTR = 2
	LACE = 3
	GOTWA = 4
	SLLS = 5

class Report(Base):
	__tablename__ = "reports"

	id = Column(Integer, primary_key = True)
	recording = Column(Integer)
	category = Column(Enum(ReportCategory))
	content = Column(String(64), nullable = False)

	def __init__(self: Self, recording: int, category: ReportCategory = None, content: str = None):
		self.recording = recording
		self.category = category
		self.content = content

	def __repr__(self):
		return f"Report({self.recording}, {self.category}, {self.content})"