# import logging
# import logging.handlers
# import datetime

# logger=logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
#
# rf_handle=logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
# rf_handle.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))
#
# f_handle=logging.FileHandler('error.log')
# f_handle.setLevel(logging.ERROR)
# f_handle.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s'))
#
# logger.addHandler(rf_handle)
# logger.addHandler(f_handle)
#
# logging.debug('debug msg')
# logging.info('info msg')
# logging.warning('warming msg')
# logging.error('error msg')
# logging.critical('critical msg')


# my_format='%(asctime)s-%(filename)s-%(module)s-%(lineno)d'
#
# logging.basicConfig(
#     filename='my.log',
#     level=logging.INFO,
#     format=my_format
# )
#
# logging.info('info')
# logging.debug('debug')
# logging.warning('warming')
# logging.error('error')
# logging.critical('critical')

from util import util

logger=util.get_logger()

logger.info('test infor')
logger.debug('testlallal')

logger.info('info')
logger.debug('debug')
logger.warning('warming')
logger.error('error')
logger.critical('critical')
