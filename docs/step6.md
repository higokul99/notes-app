# 🧠 STEP 6 — DATABASE MIGRATIONS (Flask-Migrate / Alembic)

## 🎯 Objective
Replace `db.create_all()` with **version-controlled database migrations**:
- Track schema changes
- Safely update DB in future
- Follow production practice

---

## 🔹 TASK 1 — Install Dependency

```bash
pip install Flask-Migrate

Add to requirements.txt:

Flask-Migrate
🔹 TASK 2 — Create Migration Extension

Create file:
app/extensions/migrate.py

from flask_migrate import Migrate

migrate = Migrate()
🔹 TASK 3 — Initialize in App

Open:
app/init.py

Update:

from app.extensions.migrate import migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
🔹 TASK 4 — Set FLASK_APP

In terminal:

export FLASK_APP=run.py      # Linux/Mac
set FLASK_APP=run.py         # Windows
🔹 TASK 5 — Initialize Migration Repo
flask db init

👉 This creates:

migrations/
🔹 TASK 6 — Generate First Migration
flask db migrate -m "initial migration"

👉 Detects your Note model

🔹 TASK 7 — Apply Migration
flask db upgrade

👉 Creates tables in DB

🔹 TASK 8 — Verify

Check your PostgreSQL DB:

Table notes exists
Structure matches model
🔹 TASK 9 — Remove Old Method

❌ Remove any:

db.create_all()
🔹 TASK 10 — Future Workflow (IMPORTANT)

Whenever you change models:

flask db migrate -m "describe change"
flask db upgrade
✅ SUCCESS CRITERIA

You are done ONLY if:

migrations/ folder exists
Tables created using flask db upgrade
No use of create_all()
Migration files generated
🚫 DO NOT DO
Do NOT manually edit DB
Do NOT skip migrations after model change
Do NOT commit without testing migration
🧭 AFTER COMPLETION

Stop.

Say:
👉 "Step 6 done"

Next: Step 7 → Authentication (JWT, Users, Protected APIs)