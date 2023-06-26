import logging.config

from log_config import LOGGING
from module1 import print_hello

logging.config.dictConfig(LOGGING)

print_hello()
