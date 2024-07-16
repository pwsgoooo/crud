from sqlalchemy import Column,String #, Text,Integer
from .conn import Base
import uuid

class Members(Base):
    __tablename__ = 'members'
    id = Column(String(36),primary_key=True,default=lambda:String(uuid.uuid4))
    name = Column(String(36), nullable=False)
    content = Column(String(200), nullable=False)

    def __repr__(self):
        return f"<Members(id={self.id},name={self.name},content={self.content})>"