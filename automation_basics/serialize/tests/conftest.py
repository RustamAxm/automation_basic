from pytest import fixture
from loguru import logger
from automation_basics.serialize.serialize import Serializer

@fixture
def get_serializer():
    logger.info(f"in fixture")
    return Serializer()
