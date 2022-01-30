"""
Logging means tracking the events or steps during the execution of programme or software.

Log Levels
==========
Critical
Error
Warning
Info
Debug


29/03/2020 03:48:17 PM Sunday: INFO: Text Entered in edit box
29/03/2020 03:48:17 PM Sunday: ERROR: Unable to click on search button

"""

import logging

# filename='test.log'
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %H:%M:%S',
                    level=logging.DEBUG)

logging.critical('This is critical message')
logging.error('Tis is an error msg')
logging.warning('This is a warning msg')
logging.info('This is an info msg')
logging.debug('This is a debug message')