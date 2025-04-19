import numpy as np
from loguru import logger


class Serializer:
    """
    Простой пример сериализации байти в числа можно внести структуру и ее кастовать
    """
    s_struct = np.dtype(
        [
            ('a', np.uint8),
            ('b', np.uint32),
        ]
    )

    def __init__(self, a=0, b=0):
        """
        Простой инит  с заполнением нащей структуры которую можно сипользовать потом
        """
        self.s = np.zeros(1, dtype=self.s_struct)
        self.s['a'] = a
        self.s['b'] = b

    def serialize(self):
        """
        Сериализация
        :param vals:
        :return:
        """
        vals = self.s.tobytes()
        logger.debug(f"{vals=}")
        return vals

    def deserialize(self, a_bytes):
        """
        Десериализация
        :param a_bytes:
        :return:
        """
        vals = np.frombuffer(a_bytes, dtype=self.s_struct)
        logger.debug(f"{vals=}")
        return vals
