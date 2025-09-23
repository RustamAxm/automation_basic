import numpy as np


def get_types(s_type):
    if s_type == "uint64":
        return np.uint64
    if s_type == "uint32":
        return np.uint32
    if s_type == "uint16":
        return np.uint16
    if s_type == "uint8":
        return np.uint8


class TempGen:
    """
    Класс для динамической генерации методов
    """

    def __init__(self, dev, config):
        self.dev = dev
        for item in config:
            func = self._get_f(item)
            setattr(self, f"{item.get('name')}", func)

    def _get_f(self, item):
        """
        Генератор с чистой областью видимости для item
        """

        def func(*args):
            assert len(args) == len(item["args"])
            payload = b""
            for v1, v2 in zip(args, item["args"], strict=False):
                payload += get_types(v2["type"])(v1)
            self.dev.write(payload)
            ret = self.dev.read(item["ret"][0]["size"])
            type_ = get_types(item["ret"][0]["type"])
            return np.frombuffer(ret, dtype=type_)

        return func
