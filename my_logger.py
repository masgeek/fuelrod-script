import datetime
import logging
from os import path, mkdir, environ

from colorlog import ColoredFormatter
from dotenv import load_dotenv

load_dotenv(verbose=True)


class MyLogger:
    _logger = None
    log_level = environ.get("LOG_LEVEL", "INFO")

    def __new__(cls, *args, **kwargs):
        if cls._logger is None:
            cls._logger = super().__new__(cls, *args, **kwargs)
            cls._logger = logging.getLogger("fuelrod")
            cls._logger.setLevel(cls.log_level)

            file_fmt = logging.Formatter(
                "%(asctime)s %(levelname)s %(thread)s [%(filename)s:%(lineno)s %(funcName)s] :: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

            console_fmt = ColoredFormatter(
                fmt="%(asctime)s %(log_color)s%(levelname)-8s%(reset)s| [%(filename)s:%(lineno)s %(funcName)s]"
                "%(reset)s | %(log_color)s%(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                reset=True,
                log_colors={
                    "DEBUG": "bold_cyan",
                    "INFO": "bold_green",
                    "WARNING": "bold_yellow",
                    "ERROR": "bold_red",
                    "CRITICAL": "bold_red,bg_white",
                },
                secondary_log_colors={},
                style="%",
            )

            now = datetime.datetime.now()
            dirname = "./logs"

            if not path.isdir(dirname):
                mkdir(dirname)

            base_file_name = dirname + "/log_" + now.strftime("%Y-%m-%d") + ".log"

            info_log_file = path.join(
                path.dirname(path.abspath(__file__)), base_file_name
            )

            file_handler = logging.FileHandler(info_log_file)

            stream_handler = logging.StreamHandler()

            file_handler.setFormatter(file_fmt)
            stream_handler.setFormatter(console_fmt)

            cls._logger.addHandler(stream_handler)
            cls._logger.addHandler(file_handler)

        return cls._logger
