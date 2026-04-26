# 🧠 STEP 5 — VALIDATION & ERROR HANDLING (Agent Instructions)

## 🎯 Objective
Upgrade your API from basic CRUD → **production-level behavior**:
- Centralized error handling
- Clean validation
- Consistent API responses

---

## 🔹 TASK 1 — Create Error Handler Module

Create file:
app/errors/handlers.py

Add:

```python
from flask import jsonify

def register_error_handlers(app):

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
🔹 TASK 2 — Register Error Handlers

Open:
app/init.py

Add inside create_app():

from app.errors.handlers import register_error_handlers

register_error_handlers(app)
🔹 TASK 3 — Improve Validation in Routes

Open:
app/routes/note_routes.py

🔁 Update create_note()
data = request.get_json()

if not data:
    return jsonify({"error": "Invalid JSON data"}), 400

title = data.get("title")

if not title or not title.strip():
    return jsonify({"error": "Title is required"}), 400
🔁 Update update_note()
data = request.get_json()

if not data:
    return jsonify({"error": "Invalid JSON data"}), 400

title = data.get("title")
content = data.get("content")

if title is not None and not title.strip():
    return jsonify({"error": "Title cannot be empty"}), 400
🔹 TASK 4 — Standardize Responses

Ensure ALL responses follow:

Success:
{
  "data": {...},
  "message": "Success"
}
Error:
{
  "error": "Error message"
}
Example Update
return jsonify({
    "data": note.to_dict(),
    "message": "Note created successfully"
}), 201
🔹 TASK 5 — Handle Missing Notes Cleanly

Replace:

Note.query.get(id)

With safer logic:

note = Note.query.get(id)
if not note:
    return jsonify({"error": "Note not found"}), 404

(Ensure this is consistent across GET, PUT, DELETE)

🔹 TASK 6 — Add Try-Catch for DB Operations

Wrap DB commits:

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
    return jsonify({"error": "Database error"}), 500
🔹 TASK 7 — Run Application
python run.py
🔹 TASK 8 — Test Edge Cases (MANDATORY)

Test using Postman:

❌ Empty JSON
{}
❌ Missing title
{
  "content": "test"
}
❌ Invalid ID
GET /api/notes/9999
✅ SUCCESS CRITERIA

You are done ONLY if:

Invalid input returns 400
Missing note returns 404
DB errors handled safely
All responses follow consistent format
No raw errors exposed
🚫 DO NOT DO
Do NOT add authentication yet
Do NOT add schemas (next step)
Do NOT skip testing edge cases
🧭 AFTER COMPLETION

Stop.

Say:
👉 "Step 5 done"

Next: Step 6 → Database Migrations (Alembic / Flask-Migrate)