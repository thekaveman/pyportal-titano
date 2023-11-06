import time

import adafruit_logging as logging

from app.util import get_env

LOG_LEVEL = get_env("LOG_LEVEL", "DEBUG")
LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


class FormattedPrintHandler(logging.StreamHandler):
    """StreamHandler that formats messages with time since Board Epoch, level, and logger name.

    Board Epoch (January 1, 2000 12:00:00 AM) resets when the board is powered on.
    """

    def format(self, record):
        return f"[{time.time()}] ({record.levelname}) <{record.name}>: {record.msg}"


def configure(name="pyportal", level=None):
    """Configures the CircuitPython logging framework and returns a Logger instance."""

    level = level or LOG_LEVEL
    level = LEVELS.get(level, "DEBUG")

    logger = logging.getLogger(name)
    logger.setLevel(level)

    print_handler = FormattedPrintHandler()
    print_handler.setLevel(level)

    logger.addHandler(print_handler)

    return logger
