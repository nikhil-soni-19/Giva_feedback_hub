from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    product_id: str
    rating: int
    review_text: str
