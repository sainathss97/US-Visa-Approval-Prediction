# pylint: disable=import-error
from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
logging.info("Welcome to the 1st Log")

try:
    5/0
except Exception as e:
    logging.info(e)
    raise USvisaException(e,sys) from e

