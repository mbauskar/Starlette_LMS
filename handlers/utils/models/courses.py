import enum
from datetime import datetime

from sqlalchemy import Enum, Text, Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.db_setup import Base
from handlers.utils.models.user import User


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)


class StudentCourse(Base):
    """
    Students can be assigned to courses.
    """

    __tablename__ = "student_courses"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    completed = Column(Boolean, default=False)
