from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()



student_m2m_subject = Table(
    "student_m2m_subject",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("student_id", Integer, ForeignKey("students.id", ondelete="CASCADE")),
    Column("subject_id", Integer, ForeignKey("subjects.id", ondelete="CASCADE")),
)

class Student(Base):


    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(50), nullable=False)
    student_phone = Column(Integer)
    student_email = Column(String(50))
    subjects = relationship("Subject", secondary=student_m2m_subject, back_populates="students", passive_deletes=True)
    #group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"))

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(150), nullable=False)
    student_id = Column(Integer, ForeignKey(Student.id))


class Teacher (Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(25), nullable=False)
    teacher_phone = Column(Integer)
    teacher_email = Column(String(50))

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(150), nullable=False, unique=True)
    students = relationship("Student", secondary=student_m2m_subject, back_populates="subjects", passive_deletes=True)
    teacher_id = Column(Integer, ForeignKey(Teacher.id))
    teacher = relationship("Teacher", backref="subject")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    grade_date = Column(DateTime, default=datetime.now())#=datetime.now
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE"))