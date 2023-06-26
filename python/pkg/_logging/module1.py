

import logging

logger = logging.getLogger(__name__)

"""
NOTSET=0
DEBUG=10
INFO=20
WARN=30
ERROR=40
and CRITICAL=50.
"""

def print_hello():
    logger.debug("DEBUUUUG")
    logger.info("INFOOO")
    logger.warn("WAAARN")
    logger.error("EEEERROR")
    print('hello')
