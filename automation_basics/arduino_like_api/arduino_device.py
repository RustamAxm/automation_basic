import serial
import numpy as np
from loguru import logger

from automation_basics.common.helpers import struct_to_dict

s_struct = np.dtype([
    ('header', np.uint8),
    ('cmd', np.uint8),
    ('payload', np.uint32),
    ('err', np.uint8),
])

class ArduinoAPI:
    """
    demo API for serial device communication
    """
    def __init__(self, com, baud_rate):
        self.dev = serial.Serial(com, baudrate=baud_rate)

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
        logger.debug(f'send to device')
        tmp = np.zeros(1, dtype=s_struct)
        tmp['header'] = 10
        tmp['cmd'] = command
        self.dev.write(tmp.tobytes())
        ret = self.dev.read(s_struct.itemsize)
        vals = struct_to_dict(np.frombuffer(ret, dtype=s_struct))
        if vals['err'] == 1:
            raise ValueError(f"error in device {command=} ")
        return vals


def main():
    dev = ArduinoAPI('/tmp/ttyV0', baud_rate=9600)
    logger.info(f'A0 data = {dev.get_a0()}')
    logger.info(f'A0 data = {dev.get_a1()}')

if __name__ == '__main__':
    main()