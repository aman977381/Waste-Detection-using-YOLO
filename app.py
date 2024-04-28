from Waste_Detection.logger import logging
from Waste_Detection.exception import AppException
import sys


try:
    a = 3/"s"

except Exception as e:
    raise AppException(e,sys)