from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Self

from common_base import Base
from entities.ally import Ally
from entities.salute import SALUTE
from entities.gotwa import GOTWA
from entities.sas import SAS
from entities.report import Report
from entities.point import Point
from entities.enemy import Enemy
from entities.evacuation import Evacuation
from entities.lace import LACE
from entities.slls import SLLS
from entities.saltr import SALTR

class Context:
	def __init__(self: Self):
		self.DATABASE_URL = "postgresql://root:database_password@192.168.43.218:5432/earofnapoleon"
		self.engine = create_engine(self.DATABASE_URL)
		Base.metadata.create_all(self.engine)
		self.session = sessionmaker(bind = self.engine)()

	def reset_and_populate(self: Self):
		f6 = Ally("flota 6", 9, 9, 9, "u", 13, 10, "p", "a")
		f2 = Ally("flota 2", 10, 10, 10, "q", 13, 10, "r", "t")
		r0 = SAS(f6, 1, "trans", 3, 4, 5)
		r1 = SALUTE(f2, 100, "trans", 1000, "a", "l", "u", 10, "e")
		try:
			for x in self.session.query(Point).all():
				self.session.delete(x)
			for x in self.session.query(Report).all():
				self.session.delete(x)
			self.session.add(f2)
			self.session.add(f6)
			self.session.add(r0)
			self.session.add(r1)
			r0.apply(self.session)
			r1.apply(self.session)
			self.session.commit()
		except Exception as e:
			print(f"Failed to populate: {e}")
			self.session.rollback()
