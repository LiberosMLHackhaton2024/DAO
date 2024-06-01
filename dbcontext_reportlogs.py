from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Self

from entities.report import *
from base_reportlogs import Base

class ReportLogsContext:
	def __init__(self: Self):
		self.DATABASE_URL = "postgresql://root:database_password@192.168.23.66:5432/reportlogs"
		self.engine = create_engine(self.DATABASE_URL)
		Base.metadata.create_all(self.engine)
		self.session = sessionmaker(bind = self.engine)()

	def reset_and_populate(self: Self):
		r0 = SALTRReport(2, "sit", "act", "loc", "tim", "rea")
		r1 = SALUTEReport(3, "siz", "act", "loc", "uni", "tim", "equ")
		try:
			# Delete all existing entries
			for x in self.session.query(Report).all():
				self.session.delete(x)
			# Add new entries
			self.session.add(r0)
			self.session.add(r1)
			self.session.commit()
		except:
			self.session.rollback()

	# def report_update(self: Self):
	# 	...
