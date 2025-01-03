from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .connection import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    text_content = Column(Text, nullable=True)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
