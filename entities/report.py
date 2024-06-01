from sqlalchemy import *
from sqlalchemy.ext.declarative import declared_attr
from typing import Self
from sqlalchemy.orm import relationship

from base_reportlogs import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    recording = Column(Integer)
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'report'
    }

    def __init__(self: Self, recording: int):
        self.recording = recording

    def __repr__(self):
        return f"Report({self.recording})"

class SALUTEReport(Report):
    __tablename__ = 'salute_reports'
    id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
    size = Column(String(64))
    activity = Column(String(64))
    location = Column(String(64))
    uniforms = Column(String(64))
    time = Column(String(64))
    equipment = Column(String(64))

    __mapper_args__ = {
        'polymorphic_identity': 'salute_report'
    }

    def __init__(self: Self, recording: int, size: str = None, activity: str = None, location: str = None, uniforms: str = None, time: str = None, equipment: str = None):
        super().__init__(recording)
        self.size = size
        self.activity = activity
        self.location = location
        self.uniforms = uniforms
        self.time = time
        self.equipment = equipment

    def __repr__(self):
        return f"SALUTEReport({self.recording}, {self.size}, {self.activity}, {self.location}, {self.uniforms}, {self.time}, {self.equipment})"

class SALTRReport(Report):
    __tablename__ = 'saltr_reports'
    id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
    situation = Column(String(64))
    action = Column(String(64))
    location = Column(String(64))
    time = Column(String(64))
    reaction = Column(String(64))

    __mapper_args__ = {
        'polymorphic_identity': 'saltr_report'
    }

    def __init__(self: Self, recording: int, situation: str = None, action: str = None, location: str = None, time: str = None, reaction: str = None):
        super().__init__(recording)
        self.situation = situation
        self.action = action
        self.location = location
        self.time = time
        self.reaction = reaction

    def __repr__(self):
        return f"SALTRReport({self.recording}, {self.situation}, {self.action}, {self.location}, {self.time}, {self.reaction})"

class LACEReport(Report):
    __tablename__ = 'lace_reports'
    id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
    liquids = Column(String(64))
    ammunition = Column(String(64))
    casualties = Column(String(64))
    equipment = Column(String(64))

    __mapper_args__ = {
        'polymorphic_identity': 'lace_report'
    }

    def __init__(self: Self, recording: int, liquids: str = None, ammunition: str = None, casualties: str = None, equipment: str = None):
        super().__init__(recording)
        self.liquids = liquids
        self.ammunition = ammunition
        self.casualties = casualties
        self.equipment = equipment

    def __repr__(self):
        return f"LACEReport({self.recording}, {self.liquids}, {self.ammunition}, {self.casualties}, {self.equipment})"

class GOTWAReport(Report):
    __tablename__ = 'gotwa_reports'
    id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
    going = Column(String(64))
    others = Column(String(64))
    time = Column(String(64))
    what = Column(String(64))
    action = Column(String(64))

    __mapper_args__ = {
        'polymorphic_identity': 'gotwa_report'
    }

    def __init__(self: Self, recording: int, going: str = None, others: str = None, time: str = None, what: str = None, action: str = None):
        super().__init__(recording)
        self.going = going
        self.others = others
        self.time = time
        self.what = what
        self.action = action

    def __repr__(self):
        return f"GOTWAReport({self.recording}, {self.going}, {self.others}, {self.time}, {self.what}, {self.action})"

class SLLSReport(Report):
    __tablename__ = 'slls_reports'
    id = Column(Integer, ForeignKey('reports.id'), primary_key=True)
    stop = Column(String(64))
    listen = Column(String(64))
    look = Column(String(64))
    smell = Column(String(64))

    __mapper_args__ = {
        'polymorphic_identity': 'slls_report'
    }

    def __init__(self: Self, recording: int, stop: str = None, listen: str = None, look: str = None, smell: str = None):
        super().__init__(recording)
        self.stop = stop
        self.listen = listen
        self.look = look
        self.smell = smell

    def __repr__(self):
        return f"SLLSReport({self.recording}, {self.stop}, {self.listen}, {self.look}, {self.smell})"
