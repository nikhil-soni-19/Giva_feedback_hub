# 💍 Giva Feedback Hub

A simple end-to-end feedback analytics system for **Giva (Jewelry Brand)** that collects customer reviews, performs rule-based sentiment and theme analysis, and displays actionable insights on a dynamic dashboard.

This project uses **no AI/ML models** — all analysis is done using **custom rule-based logic**.

---

## 📌 Features

### ✅ Backend (FastAPI)
- Submit product feedback (ring, earring, necklace)
- Rule-based sentiment analysis (Positive / Negative / Neutral)
- Rule-based theme detection:
  - Comfort
  - Durability
  - Appearance
- Product-wise feedback storage (SQLite)
- REST APIs with auto-generated Swagger docs

### ✅ Frontend (HTML, CSS, JavaScript)
- Feedback submission form
- Product-wise dashboard
- Sentiment visualization using bar charts
- Theme frequency visualization
- Product-specific insight generation
- Dynamic updates (no page reload)

---

## 🏗️ Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | FastAPI, Python |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| API Docs | Swagger (FastAPI `/docs`) |

---

## 📂 Project Structure

