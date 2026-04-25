import logging
import os
import pytz
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from flask_sqlalchemy import SQLAlchemy

tz = pytz.timezone("Asia/Kolkata")

class TZFormatter(logging.Formatter):
    def converter(self, timestamp):
        return datetime.fromtimestamp(timestamp, tz)

db = SQLAlchemy()

def setup_logging(app):
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    console = logging.StreamHandler()
    console.setLevel(app.config["LOG_LEVEL"])
    console.setFormatter(formatter)

    log_file = app.config["LOG_FILE"]
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    file_handler = TimedRotatingFileHandler(
        log_file,
        when="midnight",
        interval=1,
        backupCount=10,
        encoding="utf-8",
        utc=False,
    )
    file_handler.suffix = "%Y-%m-%d"
    file_handler.setLevel(app.config["LOG_LEVEL"])
    file_handler.setFormatter(formatter)

    app.logger.setLevel(app.config["LOG_LEVEL"])
    app.logger.addHandler(console)
    app.logger.addHandler(file_handler)
    app.logger.propagate = False