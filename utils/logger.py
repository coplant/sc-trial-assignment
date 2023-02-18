import logging
import queue
from logging.handlers import QueueListener, QueueHandler

from utils.app import BASE_DIR


class AsyncLogger:
    def __init__(self, name):
        _queue = queue.Queue(-1)
        queue_handler = QueueHandler(_queue)
        handler = logging.FileHandler(BASE_DIR / "logs" / f"{name}.log")
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
            datefmt="%d.%m.%Y %H:%M:%S"
        )
        handler.setFormatter(formatter)
        self.listener = QueueListener(_queue, handler)
        self.logger = logging.getLogger()
        self.logger.addHandler(queue_handler)
        self.logger.level = 0

    def start(self):
        self.listener.start()
        self.logger.info("Logging started")

    def stop(self):
        self.logger.info("Logging stopped")
        self.listener.stop()
