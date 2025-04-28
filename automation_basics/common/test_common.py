from automation_basics.common.helpers import struct_to_dict
import numpy as np
from loguru import logger

def test_np():
    t = np.dtype([
        ('a', np.uint8),
        ('b', np.uint32),
    ])
    data = np.zeros(1, dtype=t)
    d = struct_to_dict(data)
    logger.info(f'{d=}')
    assert 'a' in d.keys()
    assert 'b' in d.keys()
    assert d.get('a') == 0
    assert d.get('b') == 0
    assert d.get('c') is None
