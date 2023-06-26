from logging import getLogger
from logging.config import dictConfig

from log_config import LOGGING

dictConfig(LOGGING)

log = getLogger(__name__)
log.debug("foo")
log.info("bar")
log.warn("baz")
