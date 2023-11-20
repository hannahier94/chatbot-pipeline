"""
Create log class for log files
"""

import logging

def get_module_logger():
    """
    Function to create logger
    :return: logger information
    """
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('full_db_log.log')
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    return logger
