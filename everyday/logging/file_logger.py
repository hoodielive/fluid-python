import os
import logging
import account

# create logger 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'account.log')
handler = loging.FileHandler(logfile)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(messages)s')
handler.setFormatter(formatter)

# Attach the handler to the logger 
logger.addHandler(handler)
