from loguru import logger
from pytest import fixture

from automation_basics.serialize.serialize import Serializer


@fixture
def get_serializer():
    logger.info("in fixture")
    return Serializer()
