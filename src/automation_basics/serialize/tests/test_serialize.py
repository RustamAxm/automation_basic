from loguru import logger


def test_serialize(get_serializer):
    ser = get_serializer
    ser.serialize()
    logger.info(f"{ser.s=}")
    assert ser.s["a"] == 0
    assert ser.s["b"] == 0


def test_deserialize(get_serializer):
    ser = get_serializer
    b_data = b"\x00\x01\x02\x03\x04"
    ret = ser.deserialize(b_data)
    logger.info(f"{b_data=}, {ret=}")
    assert ret["a"] == 0
    assert ret["b"] == 67305985
