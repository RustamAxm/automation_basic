import numpy as np
import serial
from loguru import logger

from automation_basics.arduino_like_api.arduino_device import s_struct


def device():
    """
    Эмулируем ответ устройства по ком порту

    """
    dev = serial.Serial('/tmp/ttyV1')
    while True:
        vals = dev.readline()
        logger.info(f'{vals=}')
        payload = 'from device\n'.encode('utf-8')
        logger.info(f'send from device {payload=}')
        dev.write(payload)


def emulate_arduino():
    """
    Пример эмуляции через структуры интерфейсов
    """
    dev = serial.Serial('/tmp/ttyV1')
    logger.info("start emulate")
    while True:
        data = dev.read(s_struct.itemsize)
        vals = np.frombuffer(data, dtype=s_struct)
        logger.info(f'{vals=}')
        command = vals['cmd']
        header = vals['header']

        logger.debug(f'resv {command=}')
        if command == 0 and header == 10:
            payload = 23
            err = 0
        else:
            payload = 0
            err = 1
        tmp = np.zeros(1, dtype=s_struct)
        tmp['header'] = 10
        tmp['cmd'] = 0
        tmp['payload'] = payload
        tmp['err'] = err
        logger.info(f'send from device {tmp=}')
        dev.write(tmp.tobytes())


if __name__ == '__main__':
    emulate_arduino()
