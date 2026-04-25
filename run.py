from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app import db, setup_logging
from sqlalchemy import text

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    setup_logging(app)
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))
            app.logger.info("Database Connection OK")
        except Exception as e:
            app.logger.error("Database Connection failed", exc_info=e)

    @app.route("/")
    def hello_world():
        app.logger.info("Homepage requested")
        return "<h1>Hello, Welcome to notes App!</h>"

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)