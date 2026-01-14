from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
import models, schemas
from sentiment import analyze_sentiment
from themes import detect_themes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Giva Feedback Hub")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")


def home():
    return {"status": "Giva Feedback Hub API is running"}

# -------------------------
# Database Dependency
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------
# Submit Feedback
# -------------------------
@app.post("/feedback")
def submit_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    sentiment, pos_count, neg_count = analyze_sentiment(feedback.review_text)
    themes = detect_themes(feedback.review_text)

    new_feedback = models.Feedback(
        product_id=feedback.product_id,
        rating=feedback.rating,
        review_text=feedback.review_text,
        sentiment=sentiment,
        positive_words=pos_count,
        negative_words=neg_count,
        themes=",".join(themes)
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return {
        "message": "Feedback submitted successfully",
        "sentiment": sentiment,
        "themes": themes
    }

# -------------------------
# Fetch Feedback by Product
# -------------------------
@app.get("/feedback/{product_id}")
def get_feedback(product_id: str, db: Session = Depends(get_db)):
    feedbacks = db.query(models.Feedback).filter(
        models.Feedback.product_id == product_id
    ).all()

    response = []
    for fb in feedbacks:
        response.append({
            "id": fb.id,
            "product_id": fb.product_id,
            "rating": fb.rating,
            "review_text": fb.review_text,
            "sentiment": fb.sentiment,
            "positive_words": fb.positive_words,
            "negative_words": fb.negative_words,
            "themes": fb.themes.split(",") if fb.themes else [],
            "created_at": fb.created_at.isoformat() if fb.created_at else None
        })

    return {
        "product_id": product_id,
        "total_reviews": len(response),
        "feedbacks": response
    }

# -------------------------
# Theme Summary (Dashboard)
# -------------------------
@app.get("/themes/{product_id}")
def theme_summary(product_id: str, db: Session = Depends(get_db)):
    feedbacks = db.query(models.Feedback).filter(
        models.Feedback.product_id == product_id
    ).all()

    theme_counts = {
        "Comfort": 0,
        "Durability": 0,
        "Appearance": 0
    }

    for fb in feedbacks:
        if fb.themes:
            for theme in fb.themes.split(","):
                if theme in theme_counts:
                    theme_counts[theme] += 1

    return {
        "product_id": product_id,
        "theme_counts": theme_counts
    }
