import numpy as np
from loguru import logger

from automation_basics.common.helpers import struct_to_dict


def test_np():
    t = np.dtype(
        [
            ("a", np.uint8),
            ("b", np.uint32),
        ],
    )
    data = np.zeros(1, dtype=t)
    d = struct_to_dict(data)
    logger.info(f"{d=}")
    assert "a" in d
    assert "b" in d
    assert d.get("a") == 0
    assert d.get("b") == 0
    assert d.get("c") is None
