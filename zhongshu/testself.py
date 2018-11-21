# -*- coding: UTF-8 -*-
import logging
from log import log
a=log().deflog(logging.INFO)
a.debug('this is debug info')
a.info('this is information')
a.warning('this is warning message')
a.error('this is error message')
a.fatal('this is fatal message, it is same as logger.critical')
a.critical('this is critical message')