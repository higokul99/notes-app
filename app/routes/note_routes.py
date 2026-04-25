from flask import Blueprint, request, jsonify
from app.extensions.db import db
from app.models.note import Note

note_bp = Blueprint('notes', __name__)

# Add your routes here, for example:
@note_bp.route('/', methods=['POST'])
def create_note():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    note = Note(
        title=data["title"],
        content=data.get("content", "")
    )
    db.session.add(note)
    db.session.commit()

    return jsonify(note.to_dict()), 201