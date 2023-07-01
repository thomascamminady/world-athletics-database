import logging
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    foldername_root: Path = Path(__file__).parent.parent.parent.resolve()
    foldername_log: Path = foldername_root / "logs"
    filename_debug_log: Path = foldername_log / "debug.log"

    logger_level: int = logging.DEBUG
    logger_shell_level: int = logging.DEBUG
    logger_file_level: int = logging.DEBUG

    logger_shell_fmt: str = "%(message)s"
    logger_file_fmt: str = (
        "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] \t%(message)s"
    )


config = Config()
