import inspect
import logging


def getLogger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    fileHandler = logging.FileHandler('logfile.log')
    # fileHandler = logging.FileHandler('{0}.format(logName), mode='a')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s", datefmt='%d/%m/%y %H:%M:%S')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object
    logger.setLevel(logging.DEBUG)

    return logger

def test_logger():
    logger = getLogger()

    logger.critical('This is critical message')
    logger.error('Tis is an error msg')
    logger.warning('This is a warning msg')
    logger.info('This is an info msg')
    logger.debug('This is a debug message')