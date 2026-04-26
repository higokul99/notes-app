# 📁 Flask Notes App - Standard Project Structure (No Docker)

notes-app/
│
├── app/                          # Core application package
│   ├── __init__.py               # App factory (create_app)
│   │
│   ├── models/                   # Database models (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── note.py
│   │
│   ├── routes/                   # API routes (Blueprints)
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   └── note_routes.py
│   │
│   ├── schemas/                  # Request/response validation (Marshmallow/Pydantic)
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   └── note_schema.py
│   │
│   ├── services/                 # Business logic layer
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── note_service.py
│   │
│   ├── extensions/               # Initialize extensions (db, jwt, migrate)
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── jwt.py
│   │   └── migrate.py
│   │
│   ├── utils/                    # Helper utilities
│   │   ├── __init__.py
│   │   ├── decorators.py         # auth decorators
│   │   └── helpers.py
│   │
│   ├── errors/                   # Error handling
│   │   ├── __init__.py
│   │   └── handlers.py
│   │
│   └── config/                   # Optional app-level config split
│       └── __init__.py
│
├── migrations/                   # Alembic migrations (auto-generated)
│
├── tests/                        # Test cases
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_notes.py
│
├── instance/                     # Instance-specific configs (ignored in git)
│   └── config.py
│
├── .env                          # Environment variables (DO NOT COMMIT)
├── .env.example                  # Sample env file
│
├── config.py                     # Global config (Dev/Prod/Test)
├── run.py                        # Entry point (development)
├── wsgi.py                       # WSGI entry (production servers)
│
├── requirements.txt              # Dependencies
├── .gitignore
├── README.md
└── LICENSE