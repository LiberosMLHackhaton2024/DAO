from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Self

from mappoints.base_mappoints import Base
from mappoints.classes_mappoints.unit import Unit, ColorStatus

class DatabaseContext:
	def __init__(self: Self):
		self.DATABASE_URL = "postgresql://root:database_password@192.168.23.66:5432/database"
		self.engine = create_engine(self.DATABASE_URL)
		Base.metadata.create_all(self.engine)
		self.session = sessionmaker(bind = self.engine)()

	def reset_and_populate(self: Self):
		f2 = Unit("flota 2", ColorStatus.GREEN)
		f6 = Unit("flota 6", ColorStatus.YELLOW)
		try:
			# Delete all existing entries
			for x in self.session.query(Unit).all():
				self.session.delete(x)
			# Add new entries
			self.session.add(f2)
			self.session.add(f6)
			self.session.commit()
		except:
			self.session.rollback()

	# def report_update(self: Self):
	# 	...
