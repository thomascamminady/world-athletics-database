import logging
import os

from rich.logging import RichHandler

from world_athletics_database import config

logger = logging.getLogger(__name__)

shell_handler = RichHandler()
if not os.path.exists(config.foldername_log):
    os.makedirs(config.foldername_log)

file_handler = logging.FileHandler(config.filename_debug_log)

logger.setLevel(config.logger_level)
shell_handler.setLevel(config.logger_shell_level)
file_handler.setLevel(config.logger_file_level)


shell_formatter = logging.Formatter(config.logger_shell_fmt)
file_formatter = logging.Formatter(config.logger_file_fmt)

shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)
