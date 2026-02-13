from sqlalchemy import Column, Integer, Float, String
from database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    base_salary = Column(Float)
    overtime = Column(Float)
    bonus = Column(Float)
    deductions = Column(Float)

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Float)
    category = Column(String)
