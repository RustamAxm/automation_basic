import numpy as np


class Temp:
    def __init__(self, dev):
        self.dev = dev

    def f_first(
        self,
        a,
        b,
    ):
        payload = b""
        payload += np.uint8(a).tobytes()
        payload += np.uint32(b).tobytes()
        self.dev.write(payload)
        ret = self.dev.read(4)
        return np.frombuffer(ret, dtype=np.uint32)
