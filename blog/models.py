from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    
    creator = relationship("User", back_populates="blogs")
    user_id = Column(Integer, ForeignKey('users.id'))

    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship("Blog", back_populates="creator")