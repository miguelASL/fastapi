from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    overview = Column(String(300), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)