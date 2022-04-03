import logging
import os
import sys
from pyprojroot import here

sys.path.insert(0, os.path.join(here()))
import src.config as cfg  # this file needs to be run for setting up the logging

logger = logging.getLogger(__name__)


def check_directory(dir: str):
    """Create directory if it does not exist.
    Args:
    dir (str): relative address (from the root directory of the project)

    Returns:
    print a statement about the existance of the directory
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
        logger.info("The new directory is created!")
    else:
        logger.info("Path already exists!")

