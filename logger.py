import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)


file_handler = RotatingFileHandler(
    LOGS_DIR / "bot.log", maxBytes=1000000, backupCount=5,
)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
))

def setup_logging(level : str = "INFO"):
    logging.basicConfig(level=level, handlers=[file_handler, logging.StreamHandler()])