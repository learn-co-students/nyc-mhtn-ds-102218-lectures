# why use orms instead of 1. sql

# what is actually happening
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, Text, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
# class Base():
#     def __init__(name = )

# class Column():
#     def __init__(column_type, primary_key = False):
#         pass
# campus has many teachers
# teacher belongs to campus

# teachers
    # name | campus_id
        # avi | 1

# campuses
    # location
        # 'nyc'






class Campus(Base):
    __tablename__ = 'campuses'
    id = Column(Integer, primary_key = True)
    city = Column(Text)
    teachers = relationship('Teacher', back_populates='campus')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    campus_id = Column(Integer, ForeignKey('campuses.id'))
    campus = relationship(Campus, back_populates='teachers')

    # problem: if we teacher.campus = main_campus
    # and do not call session.commit()
    # then main_campus.teachers will not include that new teacher

    # The solution is to say whenever teacher.campus = teacher is called,
     # back_populates the campus.teachers method

     #

engine = create_engine('sqlite:///flatiron_school.db', echo = True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

session = Session()
avi = Teacher(name = 'avi')

    # Campus()
