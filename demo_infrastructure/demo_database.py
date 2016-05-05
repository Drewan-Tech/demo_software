#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


from drewantech_common.database_operations \
    import PostgresqlDatabaseManipulation
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,
                        String,
                        Boolean,
                        ForeignKey,
                        CheckConstraint)
from sqlalchemy.orm import relationship


database_name = 'demo_database'


db_connection = PostgresqlDatabaseManipulation('benton',
                                               'benton',
                                               'localhost',
                                               5432,
                                               'benton')


Base = declarative_base()


#  Needs to be defined before the Job class as the Job class
#  references this class.
class OperatingOn(Base):
  __tablename__ = 'operating_on'
  operator_id = Column(String(32), ForeignKey('job.id'), primary_key=True)
  operand_id = Column(String(32),
                      ForeignKey('job.id'),
                      CheckConstraint('operand_id != operator_id'))
  operator = relationship('Job',
                          foreign_keys=[operator_id],
                          back_populates='operators')
  operand = relationship('Job',
                         foreign_keys=[operand_id],
                         back_populates='operands')


class Job(Base):
  __tablename__ = 'job'
  id = Column(String(32), primary_key=True)
  producer = Column(String)
  is_finished = Column(Boolean)
  generated_files = relationship('GeneratedFile', back_populates='job')
  operators = relationship('OperatingOn',
                           foreign_keys=[OperatingOn.operator_id],
                           back_populates='operator')
  operands = relationship('OperatingOn',
                          foreign_keys=[OperatingOn.operand_id],
                          back_populates='operand')


class GeneratedFile(Base):
  __tablename__ = 'generated_file'
  file_name = Column(String, primary_key=True)
  job_id = Column(String(32), ForeignKey('job.id'))
  job = relationship('Job', back_populates='generated_files')


def create_database():
  db_connection.manipulate_database('CREATE', database_name)


def drop_database():
  db_connection.manipulate_database('DROP', database_name)


def create_tables():
  engine = db_connection.connect_to_database(database_name)
  Base.metadata.create_all(bind=engine)


def drop_tables():
  engine = db_connection.connect_to_database(database_name)
  Base.metadata.drop_all(bind=engine)
