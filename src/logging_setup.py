import logging
import logging.handlers
import os
import json
from typing import Any, Dict

LOG_FILE = os.getenv('BOT_LOG_FILE', 'bot.log')
LOG_LEVEL = os.getenv('BOT_LOG_LEVEL', 'INFO').upper()

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload: Dict[str, Any] = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
        }
        if record.exc_info:
            payload['exc_info'] = self.formatException(record.exc_info)
        return json.dumps(payload, default=str)

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(LOG_LEVEL)
    sh = logging.StreamHandler()
    sh.setFormatter(JsonFormatter())
    logger.addHandler(sh)
    fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)
    fh.setFormatter(JsonFormatter())
    logger.addHandler(fh)
    return logger
