#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#---------------------------------------
# controlle les functions liées aux logs
# 
# author : huet jb
#---------------------------------------

import logging
from .tools_functions import check_type, check_type_in_array

def setup_logger(logger_name: str, log_file_path: str, level: int = logging.INFO) -> logging.Logger:
    """Function to create and setup logger

    Args:
        logger_name (str): name of the logger
        log_file_path (str): link to the log file
        level (int, optional): level min of logs. Defaults to logging.INFO.

    Returns:
        logging.Logger: the created logger instance
    """
    
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    logger = logging.getLogger(check_type(logger_name, str))
    logger.setLevel(check_type(level, int))
    
    file_handler = logging.FileHandler(check_type(log_file_path, str), mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger
  
def send_log(message: str, logger_list: list, level: int = logging.INFO):
    """Function to send log to console and network

    Args:
        message (str): message to send
        logger_list (list[logging.Logger]): list of loggers to send the message
        level (int, optional): level of log. Defaults to logging.INFO.
    """      
    
    logger_list = check_type_in_array(logger_list, logging.Logger)
    for logger in logger_list:
        logger.log(check_type(level, int), check_type(message, str))
    