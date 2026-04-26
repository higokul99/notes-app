# 🧠 STEP 4 — IMPLEMENT FULL CRUD APIs (Agent Instructions)

## 🎯 Objective
Expand your API to support full CRUD operations:
- Get all notes
- Get single note
- Update note
- Delete note

---

## 🔹 TASK 1 — Update Routes File

Open:
app/routes/note_routes.py

Keep your existing `create_note()` and ADD the following APIs below it.

---

## 🔹 TASK 2 — Get All Notes

```python
@note_bp.route("/", methods=["GET"])
def get_notes():
    notes = Note.query.all()
    return jsonify([note.to_dict() for note in notes]), 200
🔹 TASK 3 — Get Single Note
@note_bp.route("/<int:id>", methods=["GET"])
def get_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({"error": "Note not found"}), 404

    return jsonify(note.to_dict()), 200
🔹 TASK 4 — Update Note
@note_bp.route("/<int:id>", methods=["PUT"])
def update_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({"error": "Note not found"}), 404

    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    if title:
        note.title = title
    if content:
        note.content = content

    db.session.commit()

    return jsonify(note.to_dict()), 200
🔹 TASK 5 — Delete Note
@note_bp.route("/<int:id>", methods=["DELETE"])
def delete_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({"error": "Note not found"}), 404

    db.session.delete(note)
    db.session.commit()

    return jsonify({"message": "Note deleted successfully"}), 200
🔹 TASK 6 — Run Application
python run.py
🔹 TASK 7 — Test All APIs

Use Postman or curl.

1. Get All Notes
GET /api/notes/
2. Get Single Note
GET /api/notes/1
3. Update Note
PUT /api/notes/1

Body:

{
  "title": "Updated Title"
}
4. Delete Note
DELETE /api/notes/1
🔹 TASK 8 — Verify Behavior
GET returns list of notes
GET (single) returns correct note or 404
PUT updates data in DB
DELETE removes note
Proper status codes (200, 404)
✅ SUCCESS CRITERIA

You are done ONLY if:

All 5 endpoints work (POST, GET, GET by id, PUT, DELETE)
Data persists correctly in DB
Error handling works for invalid IDs
API responses are clean JSON
🚫 DO NOT DO
Do NOT add authentication yet
Do NOT refactor into services yet
Do NOT add pagination yet
🧭 AFTER COMPLETION

Stop.

Say:
👉 "Step 4 done"

Next: Step 5 → Validation & Error Handling (make it production-level)