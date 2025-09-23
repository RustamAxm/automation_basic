import numpy as np
from pytest import fixture

from automation_basics.arduino_like_api.arduino_device import ArduinoAPI, s_struct


class MockDev:
    def __init__(self):
        self.dev = None
        self.last_cmd = None

    def write(self, data):
        """
        Mocked write
        """
        self.last_cmd = np.frombuffer(data, dtype=s_struct).copy()
        if self.last_cmd["cmd"] == 1:
            self.last_cmd["payload"] = 0
            self.last_cmd["err"] = 1
        if self.last_cmd["cmd"] == 0:
            self.last_cmd["payload"] = 23
            self.last_cmd["err"] = 0

    def read(self, n):
        """
        Mocked read function
        """
        tmp = np.zeros(1, dtype=s_struct)
        tmp["header"] = 10
        tmp["cmd"] = self.last_cmd["cmd"]
        tmp["payload"] = self.last_cmd["payload"]
        tmp["err"] = self.last_cmd["err"]
        return tmp.tobytes()[:n]


@fixture(scope="session")
def get_api():
    com_dev = MockDev()
    dev = ArduinoAPI(com_dev)
    return dev
