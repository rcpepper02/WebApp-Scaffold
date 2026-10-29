import logging
import signal
import time
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db.connection import SessionLocal
from app.logging_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)
running = True

def request_shutdown(signum: int, _frame: object) -> None:
    global running
    logger.info("Shutdown requested by signal %s", signum)
    running = False

def check_database() -> None:
    with SessionLocal() as db:
        db.execute(text("SELECT 1"))

def main() -> None:
    signal.signal(signal.SIGTERM, request_shutdown)
    signal.signal(signal.SIGINT, request_shutdown)
    logger.info("Worker starting")
    while running:
        try:
            check_database()
            logger.info("Database connectivity check succeeded")
        except SQLAlchemyError:
            logger.exception("Database connectivity check failed")
        for _ in range(30):
            if not running:
                break
            time.sleep(1)
    logger.info("Worker stopped")

if __name__ == "__main__":
    main()
