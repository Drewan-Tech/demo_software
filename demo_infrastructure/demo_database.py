#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED


from drewantech_common.database_operations \
    import PostgresqlDatabaseManipulation
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,
                        Integer,
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


class Job(Base):
  __tablename__ = 'job'
  id = Column(String(32), primary_key=True)
  producer = Column(String)
  producer_id = Column(String)
  is_finished = Column(Boolean)
  generated_files = relationship('GeneratedFile', back_populates='job')
  operating_on = relationship('OperatingOn')


class GeneratedFile(Base):
  __tablename__ = 'generated_file'
  file_name = Column(String, primary_key=True)
  job_id = Column(String(32), ForeignKey('job.id'))
  job = relationship('Job', back_populates='generated_files')


class OperatingOn(Base):
  __tablename__ = 'operating_on'
  operator_id = Column(String(32), ForeignKey('job.id'), primary_key=True)
  operand_id = Column(String(32),
                      ForeignKey('job.id'),
                      CheckConstraint('operand_id != operator_id'))
  operator = relationship('Job', foreign_keys=[operator_id])
  operand = relationship('Job', foreign_keys=[operand_id])


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
