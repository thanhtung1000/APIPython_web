from sqlalchemy import Column, Integer, Unicode, String, Date
from database import Base

class Sinhvien(Base):
    __tablename__ = "Sinhvien"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(Unicode(100), nullable=False)
    class_ = Column("class", Unicode(20), nullable=False)
    gender = Column(Unicode(20), nullable=False)
    birth_date = Column(Date, nullable=False)
    phone_number = Column(String(10))
    masinhvien = Column(String(20))
