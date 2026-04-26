from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from app.extensions.db import db
from app import setup_logging
from config import Config
from sqlalchemy import text

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    setup_logging(app)
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))
            app.logger.info("Database Connection OK")
        except Exception as e:
            app.logger.error("Database Connection failed", exc_info=e)

    from app.routes.note_routes import note_bp
    app.register_blueprint(note_bp, url_prefix="/api/notes")

    @app.route("/")
    def hello_world():
        app.logger.info("Homepage requested")
        return "<h1>Hello, Welcome to notes App! Use Endpoints to access CRUD</h>"

    from app.errors.handlers import register_error_handlers
    register_error_handlers(app)
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)