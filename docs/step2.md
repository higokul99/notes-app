Alright — here is **Step 2 as a strict agent-style instruction**.
Follow it line-by-line without skipping. Don’t optimize, don’t overthink — just execute.

---

# 🧠 STEP 2 — RESTRUCTURE INTO MODULAR APP (Agent Instructions)

## 🎯 Objective

Convert your current Flask app into:

* App Factory pattern
* Blueprint-based routing
* Modular structure

---

## 🔹 TASK 1 — Create Folder Structure

Inside your project root, create:

```
app/
app/models/
app/routes/
app/extensions/
```

Then create empty files:

```
app/__init__.py
app/models/__init__.py
app/routes/__init__.py
app/extensions/__init__.py
```

---

## 🔹 TASK 2 — Move Model

1. Move your existing Note model into:

```
app/models/note.py
```

2. Open `app/models/__init__.py` and add:

```python
from .note import Note
```

3. Ensure your model imports DB correctly:

```python
from app.extensions.db import db
```

---

## 🔹 TASK 3 — Create DB Extension

Create file:

```
app/extensions/db.py
```

Add:

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

---

## 🔹 TASK 4 — Refactor App Initialization

Open:

```
app/__init__.py
```

Replace everything with:

```python
from flask import Flask
from config import Config
from app.extensions.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # register routes (will add next)
    from app.routes.note_routes import note_bp
    app.register_blueprint(note_bp, url_prefix="/api/notes")

    return app
```

---

## 🔹 TASK 5 — Create Blueprint

Create file:

```
app/routes/note_routes.py
```

Add:

```python
from flask import Blueprint

note_bp = Blueprint("notes", __name__)

@note_bp.route("/", methods=["GET"])
def test_route():
    return {"message": "Notes API working"}
```

---

## 🔹 TASK 6 — Fix run.py

Open:

```
run.py
```

Replace with:

```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🔹 TASK 7 — Verify Imports (CRITICAL)

Check:

* No circular imports
* `db` always imported from `app.extensions.db`
* No direct app usage inside models

---

## 🔹 TASK 8 — Run Application

```bash
python run.py
```

---

## 🔹 TASK 9 — Test Endpoint

Use browser or Postman

```
GET http://127.0.0.1:5000/api/notes/
```

Expected response:

```json
{
  "message": "Notes API working"
}
```

---

# ✅ SUCCESS CRITERIA (DO NOT SKIP)

You are done ONLY if:

* App runs without errors
* Route `/api/notes/` works
* Model is inside `models/`
* No hardcoded app object used anywhere
* `create_app()` is used

---

# 🚫 DO NOT DO

* Do NOT add CRUD yet
* Do NOT add auth
* Do NOT over-engineer
* Do NOT skip blueprint

---

# 🧭 AFTER COMPLETION

Stop.

Do NOT continue ahead.

Come back and say:
👉 **“Step 2 done”**

Then I will give you **Step 3 (Create Note API — real backend logic)**
