# 🧠 STEP 3 — IMPLEMENT CREATE NOTE API (Agent Instructions)

## 🎯 Objective
Build your **first real API endpoint** to create a note:
- Accept JSON request
- Save note in PostgreSQL
- Return proper JSON response

---

## 🔹 TASK 1 — Update Note Model

Open:
app/models/note.py

Ensure it looks like this:

```python
from datetime import datetime
from app.extensions.db import db

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at
        }
🔹 TASK 2 — Create Database Tables

Run inside Python shell OR create temporary script:

python
from app import create_app
from app.extensions.db import db

app = create_app()

with app.app_context():
    db.create_all()

👉 This creates the notes table

🔹 TASK 3 — Implement Create Note API

Open:
app/routes/note_routes.py

Update file:

from flask import Blueprint, request, jsonify
from app.extensions.db import db
from app.models.note import Note

note_bp = Blueprint("notes", __name__)

@note_bp.route("/", methods=["POST"])
def create_note():
    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    # basic validation
    if not title:
        return jsonify({"error": "Title is required"}), 400

    note = Note(
        title=title,
        content=content
    )

    db.session.add(note)
    db.session.commit()

    return jsonify(note.to_dict()), 201
🔹 TASK 4 — Run Application
python run.py
🔹 TASK 5 — Test API (MANDATORY)

Use Postman or curl:

Endpoint
POST http://127.0.0.1:5000/api/notes/
Body (JSON)
{
  "title": "My First Note",
  "content": "Learning Flask step by step"
}
🔹 TASK 6 — Expected Response
{
  "id": 1,
  "title": "My First Note",
  "content": "Learning Flask step by step",
  "created_at": "2026-04-26T..."
}
🔹 TASK 7 — Test Validation

Send:

{
  "content": "No title"
}

Expected:

{
  "error": "Title is required"
}

Status Code: 400

✅ SUCCESS CRITERIA

You are done ONLY if:

POST request creates a record in DB
Data persists in PostgreSQL
JSON response is returned
Validation works (title required)
Status codes are correct (201, 400)
🚫 DO NOT DO
Do NOT add GET/PUT/DELETE yet
Do NOT add authentication
Do NOT over-engineer validation
Do NOT skip testing
🧭 AFTER COMPLETION

Stop.

Say:
👉 "Step 3 done"

Next: Step 4 → Full CRUD APIs