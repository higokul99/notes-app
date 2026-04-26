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

@note_bp.route("/", methods=["GET"])
def get_notes():
    notes = Note.query.all()
    return jsonify([note.to_dict() for note in notes]), 200

@note_bp.route("/<int:id>", methods=["GET"])
def get_note(id):
    note = Note.query.get(id)
    if not note:
        return jsonify({"error":"Note not found"}), 404
    return jsonify(note.to_dict()), 200

@note_bp.route("/<int:id>", methods=["PUT"])
def update_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({"error":"Note not found"}), 404

    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    if title:
        note.title = title
    if content:
        note.content = content
    
    db.session.commit()

    return jsonify(note.to_dict()), 200

@note_bp.route("/<int:id>", methods=["DELETE"])
def delete_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({"error":"Note not found"}), 404

    db.session.delete(note)
    db.session.commit()
    return jsonify({"message":"Note deleted successfully"}), 200