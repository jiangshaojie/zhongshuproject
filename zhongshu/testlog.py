# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='a')
console=logging.StreamHandler()
console.setLevel(logging.INFO)
formatter=logging.Formatter('%(name)-5s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)


logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warnning message')