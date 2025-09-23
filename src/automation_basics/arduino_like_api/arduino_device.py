import numpy as np
import serial
from loguru import logger

from automation_basics.common.helpers import struct_to_dict

s_struct = np.dtype(
    [
        ("header", np.uint8),
        ("cmd", np.uint8),
        ("payload", np.uint32),
        ("err", np.uint8),
    ]
)


class ArduinoAPI:
    """
    demo API for serial device communication
    """

    def __init__(self, dev):
        self.dev = dev

    def get_a0(self):
        """
        get from arduino A0 ADC info
        """
        return self._query(0)

    def get_a1(self):
        """
        get from arduino A0 ADC info
        """
        return self._query(1)

    def _query(self, command: int):
        """
        send to device commands
        """
        logger.debug("send to device")
        tmp = np.zeros(1, dtype=s_struct)
        tmp["header"] = 10
        tmp["cmd"] = command
        self.dev.write(tmp.tobytes())
        ret = self.dev.read(s_struct.itemsize)
        vals = struct_to_dict(np.frombuffer(ret, dtype=s_struct))
        if vals["err"] == 1:
            raise ValueError(f"error in device {command=} ")
        return vals


def main():
    com_dev = serial.Serial("/tmp/ttyV0", baudrate=9600)
    dev = ArduinoAPI(com_dev)
    logger.info(f"A0 data = {dev.get_a0()}")
    logger.info(f"A0 data = {dev.get_a1()}")


if __name__ == "__main__":
    main()
