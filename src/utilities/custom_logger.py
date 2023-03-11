import inspect
import logging
from os.path import join
import time
from settings import DIRS


def custom_logger(level=logging.INFO):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    file_name = "log_" + str(round(time.time() * 1000)) + ".txt"
    logger_path = join(DIRS['TEST'], "resources", "logs", file_name)
    file_handler = logging.FileHandler(logger_path, mode="w")
    file_handler.setLevel(level)

    formatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s",
                                  datefmt="%d/%m/%Y %H:%M:%S")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
