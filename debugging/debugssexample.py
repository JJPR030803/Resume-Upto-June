import logging
#logging.disable(level=logging.CRITICAL)
logging.basicConfig(filename='my_programLog.txt',level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')
logging.debug('Some debugging details')
logging.info('The logging module is working')
logging.warning('An error message is about to be logged.')
logging.error('An error has ocurred')
logging.critical('The program is unable to recover')
