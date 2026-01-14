from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, index=True)
    rating = Column(Integer)
    review_text = Column(Text)

    sentiment = Column(String)
    positive_words = Column(Integer)
    negative_words = Column(Integer)

    themes = Column(String)  # e.g. "Comfort,Appearance"
    created_at = Column(DateTime, default=datetime.utcnow)
