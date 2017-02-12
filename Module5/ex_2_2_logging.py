import logging
logging.basicConfig(filename='sample.log',level=logging.ERROR) #root logger
#logging.basicConfig(filename='sample.log',level=logging.ERROR) #root logger

logging.debug('To log file')
logging.info('message 1')
logging.warning('message 2')
logging.error('Error message 2')

logging.debug('Name test with name as debug0')

