import logging
import sys

LEVELS = { 'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logger = logging.getLogger()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fhandler = logging.FileHandler(filename='example3.log', mode='w')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(level)
    
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical error message')

