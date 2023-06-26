import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def test_ok():
    logger.debug("hello")
    assert 1 == 1

def test_error():
    logger.error("hello2")
    assert 1 == 2

